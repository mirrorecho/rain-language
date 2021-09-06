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
            fs'8
            )
            fs'16
            (
            e'16
            ~
            e'8
            ~
            e'4
            )
            r8
            e'8
            - \tenuto
            \<
            b16
            (
            c'16
            d'16
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
            ~
            e'4
            ds''4
            ~
            ds''8
            cs''8
            cs''16
            b'16
            ~
            b'8
            ~
            b'4
            r8
            b'8
            fs'16
            g'16
            a'16
            e''16
            ~
            e''8
            ds''8
            ~
            ds''4
            r8
            ds''8
            cs''8
            b'8
            cs''4
            ~
            cs''8
            ds''8
            r8
            fs''8
            f''8
            ds''8
            ds''16
            cs''16
            ~
            cs''8
            ~
            cs''4
            r8
            cs''8
            gs'16
            a'16
            b'16
            fs''16
            ~
            fs''8
            f''8
            ~
            f''4
            r8
            f''8
            ds''8
            cs''8
            ds''4
            ~
            ds''8
            f''8
            r2
            r1
            r1
            r8
            af'8
            ef'16
            e'16
            gf'16
            df''16
            ~
            df''8
            c''8
            ~
            c''4
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
                gs''8
                ~
                gs''8
                c''''8
                ~
                c''''8
                fs''8
                ~
                fs''8
                <gs''' c''''>8
                ~
                <gs''' c''''>2
                r1
                r1
                r1
                r1
                r1
                r1
                r1
                r2
                r8
                af''8
                g''8
                f''8
                f''16
                ef''16
                ~
                ef''8
                ~
                ef''4
                r8
                ef''8
                bf'16
                b'16
                df''16
                af''16
                ~
                af''8
                g''8
                ~
                g''4
                r8
                g''8
                f''8
                ef''8
                f''4
                ~
                f''8
                g''8
            }
            \context Staff = "Piano 2"
            {
                \time 4/4
                \clef "bass"
                gs,,2
                \clef "treble"
                a2
                fs'2
                r8
                a'8
                ~
                a'8
                b'8
                ~
                b'8
                e'8
                ~
                e'8
                gs'8
                ~
                gs'2
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}