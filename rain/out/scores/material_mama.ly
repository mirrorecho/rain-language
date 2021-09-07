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
            r1
            r1
            r1
            r1
            r8
            cs'''8
            \mf
            - \staccato
            e'''16
            - \staccato
            fs'''16
            - \staccato
            gs'''8
            - \staccato
            - \accent
            r4
            \tweak style #'cross
            c'''4
            - \accent
            ^ \markup { * }
            ^ \markup { (in any register) }
            ^ \markup { roughly on this pitch }
            ^ \markup { vocal sound into flute, }
            ^ \markup { * make a scary/scared }
            r8
            cs'''8
            - \staccato
            e'''16
            - \staccato
            fs'''16
            - \staccato
            gs'''8
            - \staccato
            - \accent
            r4
            \tweak style #'cross
            c'''4
            - \accent
            ^ \markup { * }
            r2
            fs'''2
            \mp
            \<
            ~
            fs'''2
            ~
            fs'''4
            ~
            fs'''8
            cs''''8
            \f
            - \accent
            - \staccato
            r1
            r8
            df'''8
            - \staccato
            gf'''16
            - \staccato
            af'''16
            - \staccato
            bf'''8
            - \staccato
            - \accent
            r4
            \tweak style #'cross
            c'''4
            - \accent
            ^ \markup { * }
            r4
            \tweak style #'cross
            c'''4
            - \accent
            ^ \markup { * }
            af''2
            \mf
            \<
            ef'''4
            \f
            - \accent
            - \staccato
            r4
            r2
            gf'''4
            (
            bf'''4
            - \accent
            )
            r2
            ef'''4
            (
            gf'''4
            - \accent
            )
        }
        \context PianoStaff = ""
        <<
            \context Staff = "Piano 1"
            {
                \tempo Agitated 4=144
                \time 4/4
                \clef "treble"
                <as e'>1
                :32
                \p
                \<
                as8
                \mf
                - \staccato
                ds'8
                - \staccato
                e'8
                - \staccato
                ds'8
                - \staccato
                as8
                - \staccato
                ds'8
                - \staccato
                e'8
                - \staccato
                ds'8
                - \staccato
                c'8
                - \staccato
                ds'8
                - \staccato
                e'8
                - \staccato
                ds'8
                - \staccato
                as8
                - \staccato
                ds'8
                - \staccato
                e'8
                - \staccato
                ds'8
                - \staccato
                as8
                - \staccato
                ds'8
                - \staccato
                e'8
                - \staccato
                ds'8
                - \staccato
                c'8
                - \staccato
                ds'8
                - \staccato
                e'8
                - \staccato
                ds'8
                - \staccato
                <c' ds' e'>1
                :32
                c'8
                - \staccato
                cs'8
                - \staccato
                e'8
                - \staccato
                cs'8
                - \staccato
                c'8
                - \staccato
                ds'8
                - \staccato
                e'8
                - \staccato
                ds'8
                - \staccato
                c'8
                - \staccato
                cs'8
                - \staccato
                e'8
                - \staccato
                cs'8
                - \staccato
                c'8
                - \staccato
                cs'8
                - \staccato
                e'8
                - \staccato
                cs'8
                - \staccato
                c'8
                - \staccato
                ds'8
                - \staccato
                e'8
                - \staccato
                ds'8
                - \staccato
                c'8
                - \staccato
                cs'8
                - \staccato
                e'8
                - \staccato
                cs'8
                - \staccato
                c'8
                - \staccato
                cs'8
                - \staccato
                fs'8
                - \staccato
                cs'8
                - \staccato
                c'8
                - \staccato
                cs'8
                - \staccato
                e'8
                - \staccato
                cs'8
                - \staccato
                <c' df' gf'>1
                :32
                \mp
                \<
                c'8
                \f
                - \staccato
                df'8
                - \staccato
                gf'8
                - \staccato
                df'8
                - \staccato
                c'8
                - \staccato
                df'8
                - \staccato
                gf'8
                - \staccato
                df'8
                - \staccato
                c'8
                - \staccato
                f'8
                - \staccato
                gf'8
                - \staccato
                f'8
                - \staccato
                c'8
                - \staccato
                f'8
                - \staccato
                gf'8
                - \staccato
                f'8
                - \staccato
                <c' gf'>1
                :32
                c'8
                - \staccato
                f'8
                - \staccato
                gf'8
                - \staccato
                f'8
                - \staccato
                d'8
                - \staccato
                f'8
                - \staccato
                gf'8
                - \staccato
                f'8
                - \staccato
                d'8
                - \staccato
                ef'8
                - \staccato
                gf'8
                - \staccato
                ef'8
                - \staccato
                d'8
                - \staccato
                ef'8
                - \staccato
                af'8
                - \staccato
                ef'8
                - \staccato
                d'8
                - \staccato
                g'8
                - \staccato
                af'8
                - \staccato
                g'8
                - \staccato
                e'8
                - \staccato
                g'8
                - \staccato
                af'8
                - \staccato
                g'8
                - \staccato
                e'8
                - \staccato
                f'8
                - \staccato
                af'8
                - \staccato
                f'8
                - \staccato
                e'8
                - \staccato
                f'8
                - \staccato
                bf'8
                - \staccato
                f'8
                - \staccato
                r1
                r1
                af'8
                cs''8
                d''8
                cs''8
                bf'8
                cs''8
                d''8
                cs''8
                bf'8
                b'8
                d''8
                b'8
                bf'8
                b'8
                e''8
                b'8
                r1
                bf8
                ef'8
                e'8
                ef'8
                c'8
                ef'8
                e'8
                ef'8
                c'8
                cs'8
                e'8
                cs'8
                c'8
                cs'8
                fs'8
                cs'8
                c'8
                f'8
                fs'8
                f'8
                d'8
                f'8
                fs'8
                f'8
                d'8
                ef'8
                fs'8
                ef'8
                d'8
                ef'8
                af'8
                ef'8
            }
            \context Staff = "Piano 2"
            {
                \time 4/4
                \clef "bass"
                r1
                r1
                r1
                r1
                r1
                <
                    \tweak style #'diamond
                    g,
                    \tweak style #'diamond
                    a,
                    \tweak style #'diamond
                    b,
                    \tweak style #'diamond
                    c
                    \tweak style #'diamond
                    d
                    \tweak style #'diamond
                    e
                    \tweak style #'diamond
                    f
                    \tweak style #'diamond
                    g
                    \tweak style #'diamond
                    a
                >4
                - \staccato
                - \accent
                _ \markup { * forearm on keys }
                r4
                r2
                r1
                r1
                r2
                r4
                r8
                <
                    \tweak style #'diamond
                    g,
                    \tweak style #'diamond
                    a,
                    \tweak style #'diamond
                    b,
                    \tweak style #'diamond
                    c
                    \tweak style #'diamond
                    d
                    \tweak style #'diamond
                    e
                    \tweak style #'diamond
                    f
                    \tweak style #'diamond
                    g
                    \tweak style #'diamond
                    a
                >8
                - \staccato
                - \accent
                _ \markup { * }
                r1
                r2
                r4
                <e,, e,>4
                - \accent
                - \staccato
                r4
                <gf,, gf,>4
                - \accent
                - \staccato
                r2
                <
                    \tweak style #'diamond
                    g,
                    \tweak style #'diamond
                    a,
                    \tweak style #'diamond
                    b,
                    \tweak style #'diamond
                    c
                    \tweak style #'diamond
                    d
                    \tweak style #'diamond
                    e
                    \tweak style #'diamond
                    f
                    \tweak style #'diamond
                    g
                    \tweak style #'diamond
                    a
                >4
                - \staccato
                - \accent
                _ \markup { * }
                r4
                r2
                r4
                <bf, gf>4
                - \tenuto
                - \accent
                gf,4
                (
                <d gf>4
                )
                ef4
                - \tenuto
                - \accent
                r4
                ef,4
                (
                <c ef>4
                )
                af,4
                (
                <c af>4
                )
                af,4
                (
                <e af>4
                )
                f,4
                (
                <af, f>4
                )
                f,4
                (
                <d f>4
                )
                bf,8
                <d bf>8
                bf,8
                <gf bf>8
                g,8
                <bf, g>8
                g,8
                <e g>8
                c8
                <e c'>8
                c8
                <af c'>8
                a,8
                <c a>8
                a,8
                <fs a>8
                d4
                (
                <fs d'>4
                )
                d4
                (
                <bf d'>4
                )
                b,4
                (
                <d b>4
                )
                b,4
                (
                <af b>4
                )
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}