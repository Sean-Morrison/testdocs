; NAME:
;   fitflatwidth
;
; PURPOSE:
;   Fit a traceset to the first-order corrected width of the flat field
;
; CALLING SEQUENCE:
;   widthset = fitflatwidth(flux, fluxivar, ansimage, [ fibermask, $
;    ncoeff=, sigma=, medwidth=, mask=, inmask=, double=, /quick ])
;
; INPUTS:
;   flux       - flat-field extracted flux
;   fluxivar   - corresponding inverse variance
;   ansimage   - output from extract image which contains parameter values
;
; OPTIONAL INPUTS:
;   fibermask  - nTrace bit mask, which marks bad fibers
;   ncoeff     - Order of legendre polynomial to apply to width vs. row;
;                default to 5.
;   sigma      - The SIGMA input to EXTRACT_IMAGE when determining ANSIMAGE;
;                default to 1.0 pix.  This can be a scalar, an [NFIBER] vector,
;                or an [NROW,NFIBER] array.
;   quick      - If set, then trim the input images to the central half
;                of the image and report MEDWIDTH in different regions
;
; OUTPUTS:
;   widthset   - Traceset structure containing fitted coefficients
;
; OPTION INPUTS:
;   mask      - the mask
;   inmask    - inmask for the call to xy2traceset
;   double    - input for the call to xy2traceset
;
; OPTIONAL OUTPUTS:
;   medwidth  - Median dispersion widths in each of 4 regions of the CCD
;               of the CCD, ordered LL,LR,UL,UR or L,B,T,R if /QUICK is set.
;
; COMMENTS:
;   The widths are forced to be the same as a function of row number
;   for all 20 fibers in each fiber bundle.
;
;   Used to fill flatstruct.widthset, which can then be applied
;   to object extraction (known profile widths).
;
; EXAMPLES:
;
; BUGS:
;
; PROCEDURES CALLED:
;   xy2traceset
;
; REVISION HISTORY:
;   01-Mar-2000  Written by S. Burles, FNAL
;-
;------------------------------------------------------------------------------
function fitflatwidth, flux, fluxivar, ansimage, fibermask, $
 ncoeff=ncoeff, sigma=sigma, medwidth=medwidth, mask=mask, $
 inmask=inmask, double=double, quick=quick, nbundles=nbundles, $
 bundlefibers = bundlefibers

   if (NOT keyword_set(ncoeff)) then ncoeff = 5
   if (NOT keyword_set(sigma)) then sigma = 1.0

   ntrace = (size(flux,/dimen))[1]
   nrow = (size(flux,/dimen))[0]
   numbundles = nbundles

   ;new changes so using the middle half of image
   if keyword_set(quick) then begin
       flux=flux[nrow/4.:3*nrow/4.-1,*]
       fluxivar=fluxivar[nrow/4.:3*nrow/4.-1,*]
       ansimage=ansimage[*,nrow/4.:3*nrow/4.-1]
       nrow = (size(flux,/dimen))[0]
   endif

   ;----------
   ; Generate a mask of good measurements based only upon the fibermask.

   if (NOT keyword_set(mask)) then mask = (flux GT 0) * (fluxivar GT 0) 

   if (keyword_set(fibermask)) then begin
      badflats = where(fibermask NE 0)
      if (badflats[0] NE -1) then mask[*,badflats] = 0
   endif

   ;----------
   ; Determine the widths from the output array from EXTRACT_IMAGE.

   igood = where(mask)
   widthterm = transpose(ansimage[lindgen(ntrace)*2+1,*])
   width = make_array(size=size(flux), /float)
   if (igood[0] NE -1) then $
    width[igood] = (1 + widthterm[igood] / flux[igood])

   ndim = size(sigma, /n_dimen)
   if (n_elements(sigma) EQ 1) then begin
      width = width * sigma[0]
   endif else if (ndim EQ 1) then begin
      for itrace=0, ntrace-1 do $
       width[*,itrace] = width[*,itrace] * sigma[itrace]
   endif else if (ndim EQ 2) then begin
      if (n_elements(sigma) NE n_elements(width)) then $
       message, 'Dimensions of SIGMA and WIDTH do not agree'
      width = width * sigma
   endif else begin
      message, 'Unsupported number of elements for SIGMA'
   endelse

   width = reform(width, nrow, ntrace)
   mask = reform(mask, nrow, ntrace)
   width_bundle = fltarr(nrow,numbundles)
   width_final  = fltarr(nrow,ntrace)

   mask_bundle = fltarr(nrow, numbundles)
   mask_final  = fltarr(nrow, ntrace)
   t_lo = intarr(nbundles)
   for ibun=1, nbundles-1 do t_lo[ibun]=total(bundlefibers[0:ibun-1])
   t_hi = t_lo + bundlefibers -1

   for irow=0, nrow-1 do begin
      for j=0, numbundles-1 do begin
         ss = where(mask[irow,[t_lo[j]:t_hi[j]]], ct)
         ; At least half the points should be good
	     if irow eq 2000 then splog, 'Number of Unmasked Traces: ',ct,' of ', bundlefibers[j];, ct GE 0.5*bundlefibers[j]
         if (ct GE 0.5*bundlefibers[j]) then $
           width_bundle[irow,j] = djs_median(width[irow,[t_lo[j]:t_hi[j]]]) $
         else $
          width_bundle[irow,j] = 0
         width_final[irow,[t_lo[j]:t_hi[j]]] = width_bundle[irow,j]
      endfor
   endfor

   ;----------
   ; Turn the widths back into a traceset.

   ; Generate the corresponding mask that is the same within each
   ; bundle, and marked as good if at least 25% of the points are unmasked

   if keyword_set(inmask) ne 0 then begin
       for j=0, numbundles-1 do begin
            mask_bundle[*,j] = rebin(float(inmask[*,[t_lo[j]:t_hi[j]]]), nrow, 1) GE 0.25
;            mask_final[*,[t_lo[j]:t_hi[j]]] = mask_bundle[*,j]
       endfor	    
       for irow=0, nrow-1 do begin
	   for j=0, numbundles-1 do begin
	       mask_final[irow,[t_lo[j]:t_hi[j]]] = mask_bundle[irow,j]
	   endfor
       endfor
   endif else begin
       mask_final = width_final GT 0
   endelse
;   if (keyword_set(inmask) NE 0) then begin
; 	splog, size(inmask)
;      mask_bundle = CONGRID(float(inmask), nrow, numbundles) GE 0.25
;      mask_final = CONGRID(mask_bundle, nrow, ntrace)
;	splog, size(mask_bundle)
;	splog,size(mask_final)
;   endif else begin
;      mask_final = width_final GT 0
;   endelse
   
   xy2traceset, findgen(nrow) # replicate(1,ntrace), $
    width_final, widthset, ncoeff=ncoeff, xmin=xmin, xmax=xmax, $
    inmask=mask_final, double=double

   ;----------
   ; Compute the widths in each of 4 regions on the CCD
   ; as the median of the unmasked pixels

   traceset2xy, widthset, xx, width_fit
   if keyword_set(quick) then begin
       x1 = [0,nrow/4,nrow/4,3*nrow/4]
       x2 = [nrow/4-1,3*nrow/4-1,3*nrow/4-1,nrow-1]
       y1 = [ntrace/4,0,3*ntrace/4,ntrace/4]
       y2 = [3*ntrace/4-1,ntrace/4-1,ntrace-1,3*ntrace/4-1]
       comment = '(L B T R)'
   endif else begin
       x1 = [0,0,nrow/2,nrow/2]
       x2 = [nrow/2-1,nrow/2-1,nrow-1,nrow-1]
       y1 = [0,ntrace/2,0,ntrace/2]
       y2 = [ntrace/2-1,ntrace-1,ntrace/2-1,ntrace-1]
       comment = '(LL UL LR UR)'
   endelse     
   medwidth = fltarr(4)
   for i=0,3 do begin
      indx = where(mask_final[x1[i]:x2[i],y1[i]:y2[i]],ct)
      if (ct GT 0) then $
       medwidth[i] = $
        median([ (width_fit[x1[i]:x2[i],y1[i]:y2[i]])[indx] ])
   endfor

   splog, 'Median spatial widths = ' $
    + string(medwidth,format='(4f5.2)') + ' pix ' + comment
   return, widthset
end
;------------------------------------------------------------------------------