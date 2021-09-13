%! abjad.LilyPondFile._get_format_pieces()
\version "2.22.1"
%! abjad.LilyPondFile._get_format_pieces()
\language "english"
%! abjad.LilyPondFile._get_formatted_includes()
\include "./rain-language/rain/score/stylesheets/stylesheet.ily"
%! abjad.LilyPondFile._get_formatted_includes()
\include "./rain-language/rain/score/stylesheets/stylesheet_title_spacing.ily"

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
            \time 4/4
            \clef "treble"
            R1
            r2
            r8
            a'8
            \p
            (
            gs'8
            [
            e'8
            )
            ]
            fs'16
            (
            gs'8.
            ~
            gs'4
            )
            r4
            r8
            a'8
            - \tenuto
            \<
            b'16
            (
            c''16
            d''16
            )
            a'16
            \>
            ~
            (
            a'8
            gs'8
            \!
            ~
            gs'4
            )
            r4
            r8
            gs'8
            (
            fs'8
            [
            e'8
            )
            ]
            fs'4
            ~
            (
            fs'8
            gs'8
            )
            R1
            r8
            e'8
            \<
            ~
            (
            e'4
            ds''4
            ~
            ds''8
            cs''8
            cs''16
            b''8.
            \mp
            ~
            b''4
            )
            r8
            b'8
            - \tenuto
            \<
            fs'16
            (
            g'16
            a'16
            )
            e''16
            \>
            ~
            (
            e''8
            ds''8
            \!
            ~
            ds''4
            )
            r8
            ds''8
            \<
            (
            cs''16
            [
            b''8.
            )
            ]
            cs'''16
            (
            ds'''8.
            ~
            ds'''4
            \mf
            )
            r2
            r8
            as'8
            (
            cs''16
            d''16
            e''16
            b''16
            ~
            b''8
            as''8
            ~
            as''4
            )
            r8
            as'8
            \>
            (
            gs'4
            )
            fs''4
            (
            gs''4
            ~
            gs''8
            as'8
            \pp
            ~
            as'4
            ~
            as'2
            )
        }
        \context PianoStaff = ""
        <<
            \context Staff = "Piano 1"
            \with
            {
                pedalSustainStyle = #'mixed
            }
            {
                \tempo Aloof 4=60
                \time 4/4
                \clef "treble"
                gs''2
                \pp
                gs''2
                gs''2
                gs''8
                gs''4
                \<
                c''''8
                ~
                c''''8
                fs''4
                <gs''' c''''>8
                <gs'' b'' d'''>2
                \p
                <c''' b'''>4
                ~
                <c''' b'''>8
                fs'8
                (
                gs'4
                )
                a''8
                (
                gs''8
                )
                gs''8
                gs''4
                \!
                c''''8
                ~
                c''''8
                fs''4
                <gs''' c''''>8
                <c''' gs'''>2
                gs'''2
                <e'' ds'''>4
                b''4
                cs''4
                \<
                ds'''4
                r8
                e''8
                (
                ds'''8
                b''8
                cs''8
                ds'''8
                )
                <g'' fs'''>4
                \mp
                cs''8
                ds'''8
                e''8
                ds'''8
                ds'''8
                ds'''4
                g'''8
                ~
                g'''8
                cs'''4
                <ds''' g'''>8
                r8
                b''8
                (
                as''16
                fs''8.
                gs''8
                as'8
                ~
                as'4
                b'2
                )
                r8
                as''8
                \>
                d'''4
                gs''4
                <as'' d'''>4
                ~
                <as'' d'''>8
                as''8
                \pp
                ~
                as''4
                ~
                as''2
                as''2
                as'''2
                ~
                as'''1
            }
            \context Staff = "Piano 2"
            \with
            {
                pedalSustainStyle = #'mixed
            }
            {
                \time 4/4
                \clef "bass"
                gs,,2
                a2
                \clef "treble"
                fs'2
                r8
                a'4
                b'8
                ~
                b'8
                e'4
                gs'8
                a'2
                \clef "bass"
                <d, e>4
                ~
                <d, e>8
                e,8
                fs4
                gs4
                r8
                \clef "treble"
                a'4
                b'8
                ~
                b'8
                e'4
                gs'8
                gs'2
                ds''2
                cs''4
                ds''4
                ds'4
                cs'4
                \clef "bass"
                b,4
                a,,4
                <g,, a,>4
                \clef "bass"
                <a,, b,>4
                b,8
                cs'8
                ds'4
                r8
                \clef "treble"
                e''4
                fs''8
                ~
                fs''8
                b'4
                ds''8
                as'2
                \clef "bass"
                as2
                as,2
                r8
                \clef "treble"
                b'8
                cs''4
                fs'4
                as'4
                ~
                as'8
                \clef "bass"
                as,,8
                ~
                as,,4
                ~
                as,,2
                b2
                \clef "treble"
                gs'2
                ~
                gs'1
                \bar "|."
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}