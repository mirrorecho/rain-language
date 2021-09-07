%! abjad.LilyPondFile._get_format_pieces()
\version "2.22.1"
%! abjad.LilyPondFile._get_format_pieces()
\language "english"

%! abjad.LilyPondFile._get_formatted_blocks()
\score
%! abjad.LilyPondFile._get_formatted_blocks()
{
    \context Score = ""
    <<
        \context Staff = "Flute"
        {
            \time 4/4
            \clef "treble"
            r1
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
            r8
            gs'8
            (
            fs'8
            e'8
            )
            fs'4
            ~
            (
            fs'8
            gs'8
            )
            r2
            r8
            e'8
            \p
            ~
            (
            e'4
            ds''4
            ~
            [
            ds''8
            cs''8
            )
            ]
            cs''16
            (
            b''8.
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
            (
            cs''8
            b'8
            )
            cs''8
            (
            ds''8
            ~
            ds''4
            )
            r8
            b'8
            as'8
            fs'8
            gs'16
            as'8.
            ~
            as'4
            r8
            fs'8
            cs'16
            d'16
            e'16
            b'16
            ~
            b'8
            as'8
            ~
            as'4
            r8
            as'8
            gs'8
            fs'8
            gs'4
            ~
            gs'8
            as'8
        }
        \context PianoStaff = ""
        <<
            \context Staff = "Piano 1"
            {
                \time 4/4
                \clef "treble"
                gs''2
                \pp
                gs''2
                gs''2
                gs''8
                gs''4
                c''''8
                ~
                c''''8
                fs''4
                <gs''' c''''>8
                <b'' d'''>4
                <c''' b'''>4
                fs'8
                gs'8
                a''8
                gs''8
                gs''8
                gs''4
                c''''8
                ~
                c''''8
                fs''4
                <gs''' c''''>8
                <c''' gs'''>4
                gs'''4
                <e'' ds'''>4
                b''4
                cs''4
                ds'''4
                r8
                e''8
                (
                ds'''8
                b''8
                cs''8
                ds'''8.
                ~
                ds'''4
                )
                <g'' fs'''>4
                cs''8
                ds'''8
                e''8
                ds'''8
                r2
                r1
                r1
                r2
                r8
                gf''8
                f''8
                df''8
                ef''16
                f''8.
                ~
                f''4
                r8
                df''8
                af'16
                a'16
                b'16
                gf''16
                ~
                gf''8
                f''8
                ~
                f''4
                r8
                f''8
                ef''8
                df''8
                ef''4
                ~
                ef''8
                f''8
            }
            \context Staff = "Piano 2"
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
                <a' gs''>4
                \clef "bass"
                <d, e>4
                e,8
                fs8
                gs4
                r8
                \clef "treble"
                a'4
                b'8
                ~
                b'8
                e'4
                gs'8
                gs'4
                ds''4
                r1
                r2
                r4
                \clef "bass"
                <a, b>4
                b,8
                cs'8
                ds'4
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}