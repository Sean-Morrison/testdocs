;+
; NAME:
;   apo_plotbias
;
; PURPOSE:
;   Plot the histogram of bias values for all 4 cameras of a single exposure
;
; CALLING SEQUENCE:
;   apo_plotbias, expnum, [ plotfile= ]
;
; INPUTS:
;   expnum     - Exposure number
;
; OPTIONAL INPUTS:
;   plotfile   - Plot file; if set, then send plot to this PostScript file
;                rather than to the default (X) display.
;
; OUTPUT:
;
; OPTIONAL OUTPUTS:
;
; COMMENTS:
;   The histogram of bias values is plotted for all (4) camera files that
;   match the given exposure number.
;
;   A fiducial line is drawn as a thick blue line.  This line approximates
;   what we expect to see for each camera.
;
;   If $BOSS_SPECTRO_DATA is not set, then it is assumed to be
;     /data/spectro
;
; EXAMPLES:
;
; BUGS:
;
; PROCEDURES CALLED:
;   dfpsclose
;   dfpsplot
;   djs_filepath()
;   djs_icolor()
;   djs_xyouts
;   fileandpath()
;   headfits()
;   plothist
;   quickbias
;   sdssproc
;   struct_append()
;   sxpar()
;
; REVISION HISTORY:
;   06-Dec-2000  Written by D. Schlegel, Princeton
;-
;------------------------------------------------------------------------------
pro apo_plotbias, expnum, plotfile=plotfile
    sos_plotbias, expnum, plotfile=plotfile
    return
end
;------------------------------------------------------------------------------
