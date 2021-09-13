%! abjad.LilyPondFile._get_format_pieces()
\version "2.22.1"
%! abjad.LilyPondFile._get_format_pieces()
\language "english"
%! abjad.LilyPondFile._get_formatted_includes()
\include "./rain-language/rain/score/stylesheets/stylesheet.ily"
%! abjad.LilyPondFile._get_formatted_includes()
\include "./rain-language/rain/score/stylesheets/stylesheet_title_coming.ily"

%! abjad.LilyPondFile._get_formatted_blocks()
\score
%! abjad.LilyPondFile._get_formatted_blocks()
{
    \context Score = ""
    <<
        \context Staff = "Flute"
        \with
        {
            pedalSustainStyle = #'mixed
        }
        {
            \tempo 4=112
            \time 4/4
            \clef "treble"
            \tweak style #'cross
            g'4
            ^ \markup { (click track...) }
            \tweak style #'cross
            d'4
            \tweak style #'cross
            g'4
            \tweak style #'cross
            d'4
            R1
            R1
            R1
            R1
            R1
            r8
            b'8
            \p
            (
            cs''8
            d''8
            ~
            d''2
            )
            R1
            \fermata
            R1
            r8
            b'8
            (
            cs''8
            d''8
            ~
            d''2
            )
            r8
            b'8
            (
            cs''8
            d''8
            ~
            d''4
            e''4
            ~
            e''2
            )
            r2
            \fermata
            r8
            b'8
            (
            cs''8
            d''8
            ~
            d''2
            )
            r8
            b'8
            (
            cs''8
            d''8
            ~
            d''4
            e''4
            ~
            e''2
            )
            r4
            e''4
            (
            g''4
            ~
            g''8
            f''8
            ~
            f''4
            e''4
            ~
            e''8
            )
            r8
            r4
            r2
            r8
            d''8
            (
            e''8
            f''8
            ~
            f''2
            )
            r8
            d''8
            (
            e''8
            f''8
            ~
            f''4
            g''4
            ~
            g''2
            )
            r4
            g''4
            (
            bf''4
            ~
            bf''8
            af''8
            ~
            af''4
            g''4
            ~
            g''8
            )
            r8
            bf''4
            (
            f''4
            bf''4
            ~
            bf''1
            )
            R1
            r4
            c'''4
            \<
            ~
            c'''2
            ef'''1
            \mf
            r4
            af''4
            \>
            (
            gf''4
            ef''4
            \!
            ~
            ef''1
            )
            r2
            gs''2
            \<
            b''1
            \f
            r4
            b'4
            a''4
            ~
            fs'''4
            r2
            r4
            b''4
            (
            d'''4
            c'''4
            b''2
            )
            r4
            r8
            b'8
            (
            d''8
            cs'''8
            ~
            cs'''4
            )
            r8
            b''8
            (
            cs'''8
            d'''8
            ~
            d'''4
            )
            e'''4
            ~
            e'''2
            r4
            e'''4
            g'''1
            r4
            e''4
            \>
            g''2
            ~
            g''2
            r4
            e'4
            g'1
            \p
            \fermata
            \bar "|."
        }
        \context PianoStaff = ""
        <<
            \context Staff = "Piano 1"
            \with
            {
                pedalSustainStyle = #'mixed
            }
            {
                \time 4/4
                \clef "treble"
                \tweak style #'cross
                g'4
                ^ \markup { (click track...) }
                \tweak style #'cross
                d'4
                \tweak style #'cross
                g'4
                \tweak style #'cross
                d'4
                r4
                <a d'>4
                ~
                <a d'>4
                <b d'>4
                ~
                <b d'>4
                <cs' d'>4
                ~
                <cs' d'>4
                <d' e'>4
                ~
                <d' e'>4
                <d' g'>4
                ~
                <d' g'>4
                <g f'>4
                ~
                <g f'>4
                <d' e'>4
                ~
                <d' e'>4
                <a d'>4
                r4
                <a d'>4
                ~
                <a d'>4
                <b d'>4
                ~
                <b d'>4
                <cs' d'>4
                ~
                <cs' d'>2
                R1
                \fermata
                r4
                <a d'>4
                ~
                <a d'>4
                <b d'>4
                ~
                <b d'>4
                <cs' d'>4
                ~
                <cs' d'>2
                <d' e'>2
                <d' g'>2
                <g f'>2
                r2
                \fermata
                r4
                <cs' d'>4
                ~
                <cs' d'>4
                <d' e'>4
                ~
                <d' e'>4
                <d' g'>4
                ~
                <d' g'>2
                <g f'>2
                <d' e'>2
                <a d'>1
                ~
                <a d'>4
                r4
                r2
                r4
                <a' d''>4
                ~
                <a' d''>4
                <d'' f''>4
                ~
                <d'' f''>4
                <e'' f''>4
                ~
                <e'' f''>4
                <f'' g''>4
                ~
                <f'' g''>4
                <f'' bf''>4
                ~
                <f'' bf''>2
                <bf' af''>2
                <f'' g''>2
                <c'' f''>1
                <c'' ef'' f''>1
                r8
                g''8
                (
                ]
                bf''8
                [
                <a'' a'''>8
                ~
                ]
                <a'' a'''>4
                ~
                <a'' a'''>8
                <c'' c'''>8
                ~
                <c'' c'''>2
                )
                r4
                <c'' c'''>4
                (
                ef''4
                ~
                ef''8
                df'''8
                ~
                df'''4
                <c''' c''''>4
                )
                r8
                <c' af' c''>8
                ~
                (
                <c' af' c''>8
                <ef' ef''>8
                ~
                <ef' ef''>8
                <d'' d'''>8
                ~
                <d'' d'''>4
                ~
                <d'' d'''>1
                )
                r8
                <ef' ef''>8
                (
                <gf' gf''>8
                <f'' f'''>8
                ~
                <f'' f'''>4
                <af'' af'''>4
                )
                r4
                <gs gs'>4
                (
                <b b'>4
                ~
                <b b'>8
                <a' a''>8
                ~
                <a' a''>4
                <gs'' gs'''>4
                ~
                <gs'' gs'''>2
                )
                r8
                <a e' a'>4
                (
                <fs' a' d''>8
                ~
                <fs' a' d''>8
                <a' gs'' a''>4
                <b' a'' b''>8
                ~
                <b' a'' b''>8
                <d'' a'' d'''>4
                <d'' c'''>8
                ~
                <d'' c'''>8
                <b'' a''' b'''>4
                <e''' a'''>8
                )
                r8
                <a d' e'>4
                (
                <b d' g'>8
                ~
                <b d' g'>8
                <g' cs'' d''>4
                <g' d'' e''>8
                ~
                <g' d'' e''>8
                <g' d'' g''>4
                <g' f''>8
                ~
                <g' f''>8
                <g' d'' e''>8
                ~
                <g' d'' e''>4
                )
                r4
                <a d' g'>4
                ~
                <a d' g'>4
                <b d' g'>4
                \>
                ~
                <b d' g'>4
                <cs' d' g'>4
                ~
                <cs' d' g'>4
                <d' e' g'>4
                ~
                <d' e' g'>4
                <d' g' d''>4
                ~
                <d' g' d''>4
                <g' f''>4
                ~
                <g' f''>4
                <d'' e''>4
                ~
                <d'' e''>4
                <a' d'' e''>4
                <g' g''>1
                \fermata
                \pp
                \bar "|."
            }
            \context Staff = "Piano 2"
            \with
            {
                pedalSustainStyle = #'mixed
            }
            {
                \time 4/4
                \clef "bass"
                R1
                g,1
                ^ \p
                g,1
                g,1
                g,2
                g,2
                g,1
                g,1
                R1
                \fermata
                g,1
                g,2
                g,2
                g,2
                g,2
                g,2
                r2
                \fermata
                r2
                g,2
                g,2
                g,2
                g,1
                g,2
                g,2
                ~
                g,4
                r4
                r2
                r2
                <g, d>2
                g,2
                f,2
                d,2
                <c, af,>2
                bf,,2
                <bf,, f,>2
                bf,,2
                <bf,, f,>2
                bf,,2
                <bf,, f,>2
                ~
                <bf,, f,>4
                <bf,, f,>4
                <bf,, f,>4
                <bf,, f,>4
                <ef,, ef,>2
                <ef,, ef,>2
                ~
                <ef,, ef,>4
                <ef, bf,>4
                <ef, bf,>4
                <ef, bf,>4
                ~
                <ef, bf,>4
                <bf,, bf,>4
                <af,, af,>4
                <gf,, gf,>4
                <f,, f,>2
                <ef, ef>2
                <ef, ef>4
                <df, df>4
                <af,, af,>4
                <gf,, gf,>4
                ~
                <gf,, gf,>4
                <fs, cs>4
                <fs, cs>4
                <cs, cs>4
                <cs, cs>4
                <b,, fs,>4
                <b,, fs, b,>4
                <b,, fs, b,>4
                ~
                <b,, fs, b,>4
                <e, e>4
                <b,, b,>4
                <a,, a,>4
                ~
                <a,, a,>4
                <c, c>4
                <b,, fs, b,>2
                <b,, b,>4
                <a,, e, a,>4
                <d, d>4
                <e, e>4
                <g, g>4
                <g, d g>4
                ~
                <g, d g>4
                e4
                <g, d g>2
                g,4
                e4
                <g, d>2
                g,4
                e4
                <g, d>2
                <g, d>2
                <g, d>2
                g,2
                g,1
                \fermata
                \bar "|."
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}