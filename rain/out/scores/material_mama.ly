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
            ^ \markup { (vary the sound each time) }
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
            r2
            r8
            g''8
            - \staccato
            af''16
            - \staccato
            bf''16
            - \staccato
            c'''8
            - \staccato
            - \accent
            r8
            g''8
            - \staccato
            af''16
            - \staccato
            bf''16
            - \staccato
            c'''8
            - \staccato
            - \accent
            f''4
            (
            af''4
            - \accent
            )
            r8
            f''8
            - \staccato
            bf''16
            - \staccato
            c'''16
            - \staccato
            d'''8
            - \staccato
            - \accent
            r4
            \tweak style #'cross
            gf''4
            - \accent
            ^ \markup { * }
            r4
            \tweak style #'cross
            gf''4
            - \accent
            ^ \markup { * }
            r4
            \tweak style #'cross
            gf''4
            - \accent
            ^ \markup { * }
            r8
            \tweak style #'cross
            af''8
            - \accent
            ^ \markup { * }
            r8
            \tweak style #'cross
            af''8
            - \accent
            ^ \markup { * }
            r8
            cs'''8
            - \staccato
            d'''16
            - \staccato
            e'''16
            - \staccato
            fs'''8
            - \staccato
            - \accent
            r8
            cs'''8
            - \staccato
            d'''16
            - \staccato
            e'''16
            - \staccato
            fs'''8
            - \staccato
            - \accent
            r4
            d'''4
            \p
            \<
            ~
            d'''2
            \tweak style #'cross
            bf''4
            \f
            - \accent
            ^ \markup { * }
            r4
            r2
            r1
            r4
            \tweak style #'cross
            c'''4
            - \accent
            ^ \markup { * }
            r2
            r2
            r4
            \tweak style #'cross
            c'''4
            - \accent
            ^ \markup { * }
            r4
            \tweak style #'cross
            d'''4
            - \accent
            ^ \markup { * }
            r4
            \tweak style #'cross
            d'''4
            - \accent
            ^ \markup { * }
            r1
            \tweak style #'diamond
            bf'1
            \fermata
            \f
            ^ \markup { (air tones only) }
            ^ \markup { hyperventilate into flute! }
            \bar "|."
        }
        \context PianoStaff = ""
        <<
            \context Staff = "Piano 1"
            {
                \tempo Agitated 4=160
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
                <e'' bf''>1
                :32
                \p
                \<
                <fs'' b'' c'''>4
                \f
                - \accent
                - \staccato
                r4
                r8
                b''8
                - \staccato
                c'''16
                - \staccato
                d'''16
                - \staccato
                e'''8
                - \staccato
                - \accent
                r8
                cs'''8
                - \staccato
                d'''8
                - \staccato
                cs'''8
                - \staccato
                as''8
                - \staccato
                cs'''8
                - \staccato
                d'''8
                - \staccato
                cs'''8
                - \staccato
                <gs'' cs''' d'''>1
                :32
                \p
                \<
                r8
                cs'''8
                \f
                - \staccato
                d'''8
                - \staccato
                cs'''8
                - \staccato
                as''8
                - \staccato
                b''8
                - \staccato
                d'''8
                - \staccato
                b''8
                - \staccato
                as''8
                - \staccato
                ds'''8
                - \staccato
                e'''8
                - \staccato
                ds'''8
                - \staccato
                c'''8
                - \staccato
                ds'''8
                - \staccato
                e'''8
                - \staccato
                ds'''8
                - \staccato
                c'''8
                - \staccato
                cs'''8
                - \staccato
                e'''8
                - \staccato
                cs'''8
                - \staccato
                c'''8
                - \staccato
                cs'''8
                - \staccato
                fs'''8
                - \staccato
                cs'''8
                - \staccato
                c'''8
                - \staccato
                f'''8
                - \staccato
                gf'''8
                - \staccato
                f'''8
                - \staccato
                d'''8
                - \staccato
                f'''8
                - \staccato
                gf'''8
                - \staccato
                f'''8
                - \staccato
                d'''8
                - \staccato
                ef'''8
                - \staccato
                gf'''8
                - \staccato
                ef'''8
                - \staccato
                d'''8
                - \staccato
                ef'''8
                - \staccato
                af'''8
                - \staccato
                ef'''8
                - \staccato
                r4
                <
                    \tweak style #'diamond
                    d'
                    \tweak style #'diamond
                    e'
                    \tweak style #'diamond
                    f'
                    \tweak style #'diamond
                    g'
                    \tweak style #'diamond
                    a'
                    \tweak style #'diamond
                    b'
                    \tweak style #'diamond
                    c''
                    \tweak style #'diamond
                    d''
                    \tweak style #'diamond
                    e''
                    \tweak style #'diamond
                    f''
                >4
                - \staccato
                - \accent
                ^ \markup { * }
                ^ \markup { with the pedal }
                ^ \markup { the tail of the sound }
                ^ \markup { try to capture only }
                r2
                <d'' af''>1
                :32
                \fermata
                \ppp
                \bar "|."
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
                - \staccato
                <d bf>8
                - \staccato
                bf,8
                - \staccato
                <gf bf>8
                - \staccato
                g,8
                - \staccato
                <bf, g>8
                - \staccato
                g,8
                - \staccato
                <e g>8
                - \staccato
                c8
                - \staccato
                <e c'>8
                - \staccato
                c8
                - \staccato
                <gs c'>8
                - \staccato
                a,8
                - \staccato
                <c a>8
                - \staccato
                a,8
                - \staccato
                <fs a>8
                - \staccato
                <d, d>4
                - \accent
                - \staccato
                r4
                d,4
                (
                <as, d>4
                )
                <cs d gs>1
                :32
                \p
                \<
                r4
                <d, d>4
                - \accent
                - \staccato
                r4
                <d, d>4
                - \accent
                - \staccato
                as,,8
                - \staccato
                ds,8
                - \staccato
                e,8
                - \staccato
                ds,8
                - \staccato
                c,8
                - \staccato
                ds,8
                - \staccato
                e,8
                - \staccato
                ds,8
                - \staccato
                r4
                <e,, e,>4
                - \accent
                - \staccato
                c,8
                - \staccato
                cs,8
                - \staccato
                fs,8
                - \staccato
                cs,8
                - \staccato
                c,8
                - \staccato
                f,8
                - \staccato
                gf,8
                - \staccato
                f,8
                - \staccato
                r4
                <gf,, gf,>4
                - \accent
                - \staccato
                r4
                <gf,, gf,>4
                - \accent
                - \staccato
                r4
                <gf,, gf,>4
                - \accent
                - \staccato
                r4
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
                \sustainOn
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}