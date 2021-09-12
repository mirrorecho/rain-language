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
            \tempo Intense 4=126
            \time 4/4
            \clef "treble"
            f''8.
            d''16
            ~
            d''8
            f''8
            d''8
            f''8
            r4
            d''8.
            f''16
            ~
            f''8
            d''8
            f''8
            d''8
            r4
            b''1
            \p
            \<
            f'''8.
            d'''16
            ~
            d'''4
            ~
            d'''4
            r4
            f'''8.
            d'''16
            ~
            d'''4
            ~
            d'''4
            r4
            c'''8.
            (
            a''16
            ~
            a''8
            )
            fs''8
            ~
            (
            fs''16
            a''8.
            )
            d''16
            (
            c''8.
            )
            b'8.
            (
            a'16
            ~
            a'8
            )
            c'8
            ~
            c'4
            r4
            r1
            r1
            r1
            r2
            b''4
            \mf
            \<
            ~
            b''8
            gs'''8
            \f
            - \accent
            - \staccato
            r4
            fs'''4
            - \tenuto
            cs'''4
            - \tenuto
            a''4
            - \tenuto
            r4
            r8
            a''8
            - \tenuto
            ~
            a''8
            fs''8
            - \tenuto
            b''4
            - \tenuto
            cs'''8.
            - \tenuto
            cs'''16
            - \tenuto
            ~
            cs'''8
            cs'''8
            - \tenuto
            ~
            cs'''8
            cs'''8
            - \tenuto
            cs'''4
            - \tenuto
        }
        \context PianoStaff = ""
        <<
            \context Staff = "Piano 1"
            {
                \clef "treble"
                ef'8
                (
                [
                g'8
                ]
                ef'8
                [
                g'8
                )
                ]
                f'8
                (
                [
                a'8
                ]
                f'8
                [
                a'8
                )
                ]
                g'8
                (
                [
                b'8
                ]
                g'8
                [
                b'8
                )
                ]
                a'8
                (
                [
                c''8
                )
                ]
                b'8
                (
                [
                d''8
                ]
                b'8
                [
                d''8
                )
                ]
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
                ]
                d''8
                [
                f''8
                )
                ]
                <b' g''>1
                <b' g''>1
                <fs' e''>1
                <gs' e''>1
                ~
                <gs' e''>1
                <c'' c'''>8.
                - \tenuto
                <a' a''>16
                - \tenuto
                ~
                <a' a''>8
                <fs' fs''>8
                - \tenuto
                ~
                <fs' fs''>8
                <a' a''>8
                - \tenuto
                <d'' d'''>4
                - \tenuto
                <b' b''>8.
                - \tenuto
                <a' a''>16
                - \tenuto
                ~
                <a' a''>8
                <c'' c'''>8
                - \tenuto
                ~
                <c'' c'''>8
                <a' a''>8
                - \tenuto
                r4
                r8
                <fs' a' fs''>8
                \mp
                - \tenuto
                \<
                ]
                <fs' a' fs''>8
                - \tenuto
                [
                <fs' a' fs''>8
                - \tenuto
                ]
                <gs' b' gs''>8
                - \tenuto
                [
                <gs' b' gs''>8
                - \tenuto
                ]
                <gs' b' gs''>8
                - \tenuto
                - \accent
                [
                <gs' b' gs''>8
                \f
                - \staccato
                - \accent
                ]
                r4
                <fs' a' cs''>4
                ~
                <fs' a' cs''>2
                r4
                fs'8
                (
                [
                a'8
                )
                ]
                gs'8
                (
                [
                b'8
                )
                ]
                a'8
                (
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
                ds''8
                (
                [
                fs''8
                )
                ]
                f''8
                (
                [
                gs''8
                )
                ]
            }
            \context Staff = "Piano 2"
            {
                \time 4/4
                \clef "bass"
                ef8
                (
                [
                g8
                ]
                ef8
                [
                g8
                )
                ]
                f8
                (
                [
                a8
                ]
                f8
                [
                a8
                )
                ]
                g8
                (
                [
                b8
                ]
                g8
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
                ]
                b8
                [
                d'8
                )
                ]
                c'8
                (
                [
                ef'8
                )
                ]
                d'8
                (
                [
                f'8
                ]
                d'8
                [
                f'8
                )
                ]
                <g g'>1
                <g g'>1
                <a e'>1
                <a e'>1
                ~
                <a e'>1
                <a e'>4
                - \tenuto
                <a e'>4
                - \tenuto
                <a e'>4
                - \tenuto
                <a e'>4
                - \tenuto
                <b fs'>4
                - \tenuto
                <b fs'>4
                - \tenuto
                <b fs'>4
                - \tenuto
                <b fs'>4
                - \tenuto
                r8
                <e, e>8
                - \tenuto
                ]
                <e, e>8
                - \tenuto
                [
                <e, d>8
                - \tenuto
                ]
                <e, d>8
                - \tenuto
                [
                <e, d>8
                - \tenuto
                ]
                <e, d>8
                - \tenuto
                - \accent
                [
                <e, d>8
                - \staccato
                - \accent
                ]
                r4
                <fs, fs>4
                - \tenuto
                <cs, cs>4
                - \tenuto
                <a,, a,>4
                - \tenuto
                r4
                fs,8
                (
                [
                a,8
                )
                ]
                gs,8
                (
                [
                b,8
                )
                ]
                a,8
                (
                [
                cs8
                )
                ]
                b,8
                (
                [
                ds8
                )
                ]
                cs8
                (
                [
                f8
                )
                ]
                ds8
                (
                [
                fs8
                )
                ]
                f8
                (
                [
                gs8
                )
                ]
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}