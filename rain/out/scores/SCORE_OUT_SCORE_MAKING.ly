%! abjad.LilyPondFile._get_format_pieces()
\version "2.22.1"
%! abjad.LilyPondFile._get_format_pieces()
\language "english"
%! abjad.LilyPondFile._get_formatted_includes()
\include "./rain-language/rain/score/stylesheets/stylesheet.ily"
%! abjad.LilyPondFile._get_formatted_includes()
\include "./rain-language/rain/score/stylesheets/stylesheet_title_making.ily"

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
            \tempo Simmering 4=96
            \time 4/4
            \clef "treble"
            \tweak style #'cross
            c''4
            ^ \markup { (click track...) }
            \tweak style #'cross
            g'4
            \tweak style #'cross
            c''4
            \tweak style #'cross
            g'4
            ef'8.
            :32
            :32
            \mp
            ^ \markup { flz. }
            c'16
            :32
            ~
            c'2
            :32
            ~
            c'8
            :32
            :32
            r8
            ef'8.
            :32
            :32
            c'16
            :32
            ~
            c'2
            :32
            ~
            c'8
            :32
            :32
            r8
            ef'8.
            :32
            :32
            c'16
            :32
            ~
            c'4
            :32
            ~
            c'8
            :32
            :32
            r8
            g'4
            :32
            :32
            ef'8.
            :32
            :32
            c'16
            :32
            ~
            c'4
            :32
            ~
            c'8
            :32
            :32
            r8
            f'4
            :32
            :32
            b'1
            :32
            :32
            a'8.
            :32
            :32
            fs'16
            :32
            ~
            fs'2
            :32
            ~
            fs'8
            :32
            :32
            r8
            b'1
            \pp
            ^ \markup { (normal) }
            \<
            ef''8.
            :32
            :32
            \mf
            ^ \markup { flz. }
            c''16
            :32
            ~
            c''4
            :32
            ~
            c''8
            :32
            :32
            r8
            a''4
            :32
            :32
            ef''8.
            :32
            :32
            c''16
            :32
            ~
            c''4
            :32
            ~
            c''8
            :32
            :32
            r8
            b''4
            :32
            :32
            a''8
            - \tenuto
            ^ \markup { (normal) }
            r8
            r4
            r4
            e'''16
            (
            d'''8.
            )
            d'''8.
            - \tenuto
            b''16
            - \tenuto
            ~
            b''8
            d'''8
            - \tenuto
            b''8
            - \tenuto
            d'''8
            - \tenuto
            r4
            r4
            fs''4
            - \tenuto
            cs''4
            - \tenuto
            a'4
            - \tenuto
            R1
            r2
            b''2
            :32
            ^ \markup { flz. }
            \<
            ~
            b''2
            :32
            :32
            gs''4
            ^ \markup { (normal) }
            ~
            gs''8
            f'''8
            \f
            - \accent
            - \staccato
            r4
            c'''4
            - \tenuto
            g''4
            - \tenuto
            ef''4
            - \tenuto
            R1
            g''8.
            - \tenuto
            g''16
            - \tenuto
            ~
            g''8
            g''8
            - \tenuto
            ~
            g''8
            g''8
            - \tenuto
            g''4
            - \tenuto
            r8
            [
            b''8
            \mp
            - \tenuto
            \<
            ]
            b''8
            - \tenuto
            [
            b''8
            - \tenuto
            ]
            f'''8
            - \tenuto
            [
            f'''8
            - \tenuto
            ]
            b'''8
            - \tenuto
            - \accent
            [
            b'''8
            \f
            - \staccato
            - \accent
            ]
            R1
            R1
            R1
            R1
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
                c''4
                ^ \markup { (click track...) }
                \tweak style #'cross
                g'4
                \tweak style #'cross
                c''4
                \tweak style #'cross
                g'4
                R1
                R1
                R1
                R1
                <b' f''>1
                \p
                fs''8
                (
                [
                a''8
                ]
                fs''8
                [
                a''8
                )
                ]
                gs''8
                (
                [
                b''8
                ]
                gs''8
                [
                b''8
                )
                ]
                a''8
                (
                [
                cs'''8
                ]
                a''8
                [
                cs'''8
                )
                ]
                b''8
                \<
                (
                [
                ds'''8
                )
                ]
                cs'''8
                (
                [
                f''8
                )
                ]
                ef''8.
                \mp
                (
                c''16
                ~
                c''8
                )
                a'8
                ~
                (
                a'16
                c'8.
                )
                f'16
                (
                ef'8.
                )
                d'8.
                \<
                (
                c'16
                ~
                c'8
                )
                ef'8
                ~
                (
                ef'16
                c'8.
                )
                f'16
                (
                g'8.
                )
                c'4
                - \tenuto
                d'4
                \mf
                - \tenuto
                <e' e''>4
                - \tenuto
                <fs' fs''>4
                - \tenuto
                r8
                [
                gs''8
                - \tenuto
                ]
                gs''8
                - \tenuto
                [
                gs''8
                - \tenuto
                ]
                gs''8
                - \tenuto
                [
                gs''8
                - \tenuto
                ]
                gs''8
                - \tenuto
                - \accent
                [
                gs''8
                - \staccato
                - \accent
                ]
                r4
                <fs' a' cs''>4
                ~
                <fs' a' cs''>2
                fs'8
                (
                [
                a'8
                ]
                fs'8
                [
                a'8
                )
                ]
                gs'8
                (
                [
                b'8
                ]
                gs'8
                [
                b'8
                )
                ]
                a'8
                (
                [
                cs''8
                ]
                a'8
                [
                cs''8
                )
                ]
                b'8
                (
                [
                ds''8
                )
                ]
                cs''8
                (
                [
                f''8
                )
                ]
                r8
                [
                <ds' fs' ds''>8
                \mp
                - \tenuto
                \<
                ]
                <ds' fs' ds''>8
                - \tenuto
                [
                <ds' fs' ds''>8
                - \tenuto
                ]
                <f' gs' f''>8
                - \tenuto
                [
                <f' gs' f''>8
                - \tenuto
                ]
                <f' gs' f''>8
                - \tenuto
                - \accent
                [
                <f' gs' f''>8
                \f
                - \staccato
                - \accent
                ]
                r4
                <c'' ef'' g''>4
                ~
                <c'' ef'' g''>2
                r4
                c''8
                (
                [
                ef''8
                )
                ]
                d''8
                (
                [
                f''8
                )
                ]
                ef''8
                (
                [
                g''8
                )
                ]
                f''8
                (
                [
                a''8
                )
                ]
                g''8
                (
                [
                b''8
                )
                ]
                a''8
                (
                [
                c'''8
                )
                ]
                b''8
                (
                [
                d'''8
                )
                ]
                r8
                [
                <a' c'' a''>8
                \mp
                - \tenuto
                \<
                ]
                <a' c'' a''>8
                - \tenuto
                [
                <a' c'' a''>8
                - \tenuto
                ]
                <b' d'' b''>8
                - \tenuto
                [
                <b' d'' b''>8
                - \tenuto
                ]
                <b' d'' b''>8
                - \tenuto
                - \accent
                [
                <b' d'' b''>8
                \f
                - \staccato
                - \accent
                ]
                R1
                \tempo "ritard. to end"
                \clef "bass"
                c8
                \>
                (
                ef8
                g8
                c'8
                \clef "treble"
                ef'8
                g'8
                c''8
                ef''8
                g''8
                c'''8
                ef'''8
                g'''8
                \ottava 1
                c''''8
                ef''''8
                g''''8
                c'''''8
                \p
                ~
                c'''''1
                )
                \bar "|."
                \ottava 0
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
                R1
                R1
                R1
                R1
                g,,1
                R1
                r2
                <cs f gs>2
                c4
                - \tenuto
                c4
                - \tenuto
                d4
                - \tenuto
                ef4
                - \tenuto
                f4
                - \tenuto
                g4
                - \tenuto
                a4
                - \tenuto
                b4
                - \tenuto
                r4
                <a,, a,>4
                ~
                <a,, a,>2
                r8
                [
                d8
                - \tenuto
                ]
                d8
                - \tenuto
                [
                d8
                - \tenuto
                ]
                d8
                - \tenuto
                [
                d8
                - \tenuto
                ]
                d8
                - \tenuto
                - \accent
                [
                d8
                - \staccato
                - \accent
                ]
                \clef "bass"
                <fs, fs>1
                fs,4
                - \tenuto
                fs,4
                - \tenuto
                gs,4
                - \tenuto
                gs,4
                - \tenuto
                a,4
                - \tenuto
                a,4
                - \tenuto
                b,4
                - \tenuto
                cs4
                - \tenuto
                r8
                [
                <cs, cs>8
                - \tenuto
                ]
                <cs, cs>8
                - \tenuto
                [
                <cs, b,>8
                - \tenuto
                ]
                <cs, b,>8
                - \tenuto
                [
                <cs, b,>8
                - \tenuto
                ]
                <cs, b,>8
                - \tenuto
                - \accent
                [
                <cs, b,>8
                - \staccato
                - \accent
                ]
                r4
                <c c'>4
                - \tenuto
                <g, g>4
                - \tenuto
                <ef, ef>4
                - \tenuto
                r4
                c8
                (
                [
                ef8
                )
                ]
                d8
                (
                [
                f8
                )
                ]
                ef8
                (
                [
                g8
                )
                ]
                f8
                (
                [
                a8
                )
                ]
                g8
                (
                [
                b8
                )
                ]
                a8
                (
                [
                c'8
                )
                ]
                b8
                (
                [
                d'8
                )
                ]
                r8
                [
                <g, g>8
                - \tenuto
                ]
                <g, g>8
                - \tenuto
                [
                <g, f>8
                - \tenuto
                ]
                <g, f>8
                - \tenuto
                [
                <g, f>8
                - \tenuto
                ]
                <g, f>8
                - \tenuto
                - \accent
                [
                <g, f>8
                - \staccato
                - \accent
                ]
                r2
                r4
                <c,, c,>4
                - \accent
                ~
                <c,, c,>1
                ~
                <c,, c,>1
                ~
                <c,, c,>1
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}