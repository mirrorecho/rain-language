#(set-default-paper-size "letter" 'portrait)
#(set-global-staff-size 21)

\header {
    composer = "Randall West"
    tagline = ##f
    % title = \markup {
    %     \column {
    %         \center-align {
    %             \fontsize #0.4 {
    %                 "Memory Bubbles I"
    %             }
    %         }
    %     }
    % }
    % piece = \markup { \box "SCORE IN C" }
    tagline = "Copyright 2021 Randall West."
    poet = ##f
}

  % #(set! paper-alist (cons '("10x13" . (cons (* 10 in) (* 13 in))) paper-alist))

  \paper {
    % #(set-paper-size "10x13")
    % system-system-spacing #'basic-distance = #9
    % system-system-spacing #'padding = #6

    % left-margin = 22\mm
    system-separator-markup = {}
    % markup-system-spacing = #'(
    %     (basic-distance . 0)
    %     (minimum-distance . 0)
    %     (padding . 8)
    %     (stretchability . 0)
    % )
    system-system-spacing = #'(
        (basic-distance . 8)
        (minimum-distance . 8)
        (padding . 8)
        (stretchability . 20)
    )
  }  

\layout {
    \set Score.markFormatter = #format-mark-circle-alphabet 
    \context {        
        \Score
        % \remove "Bar_number_engraver"
        \override MultiMeasureRest #'expand-limit = #1
        \override BarNumber #'font-size = #1.4
        \override BarNumber  #'stencil = #(make-stencil-boxer 0.1 0.25 ly:text-interface::print)
        \override RehearsalMark #'font-size = #6
    }
    \context {
        \Staff
        % \consists "Bar_number_engraver"
        % \override BarNumber #'break-visibility = #'#(#f #f #t)
        \remove Instrument_name_engraver
        \override Hairpin #'minimum-length = #7
        \override MultiMeasureRest.expand-limit = #1
    }
    \context {
        \RhythmicStaff
        % \consists "Bar_number_engraver"
        \override BarNumber #'break-visibility = #'#(#f #f #t)
        \remove Instrument_name_engraver
        \override Hairpin #'minimum-length = #6
        \override MultiMeasureRest.expand-limit = #1
    }
}