%! abjad.LilyPondFile._get_format_pieces()
\version "2.22.1"
%! abjad.LilyPondFile._get_format_pieces()
\language "english"
%! abjad.LilyPondFile._get_formatted_includes()
\include "./rain-language/rain/score/stylesheets/stylesheet.ily"
%! abjad.LilyPondFile._get_formatted_includes()
\include "./rain-language/rain/score/stylesheets/stylesheet_title_freaking.ily"

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
            \tempo Agitated 4=160
            \time 4/4
            \clef "treble"
            \tweak style #'cross
            e''4
            ^ \markup { (click track...) }
            \tweak style #'cross
            c''4
            \tweak style #'cross
            e''4
            \tweak style #'cross
            c''4
            R1
            R1
            R1
            R1
            R1
            R1
            R1
            r8
            cs'''8
            \mf
            - \staccato
            cs'''16
            - \staccato
            ds'''16
            - \staccato
            e'''8
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
            cs'''16
            - \staccato
            ds'''16
            - \staccato
            e'''8
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
            R1
            r8
            df'''8
            - \staccato
            df'''16
            - \staccato
            ef'''16
            - \staccato
            gf'''8
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
            g''16
            - \staccato
            af''16
            - \staccato
            af''8
            - \staccato
            - \accent
            r8
            g''8
            - \staccato
            g''16
            - \staccato
            af''16
            - \staccato
            af''8
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
            f''16
            - \staccato
            g''16
            - \staccato
            bf''8
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
            cs'''16
            - \staccato
            d'''16
            - \staccato
            d'''8
            - \staccato
            - \accent
            r8
            cs'''8
            - \staccato
            cs'''16
            - \staccato
            d'''16
            - \staccato
            d'''8
            - \staccato
            - \accent
            R1
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
            R1
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
            R1
            \tweak style #'diamond
            c''1
            \fermata
            \f
            ^ \markup { (air tones only) }
            ^ \markup { hyperventilate into flute }
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
                e''4
                ^ \markup { (click track...) }
                \tweak style #'cross
                c''4
                \tweak style #'cross
                e''4
                \tweak style #'cross
                c''4
                <as' e''>1
                :32
                \p
                \<
                ~
                <as' e''>1
                :32
                :32
                r8
                \mf
                ds''8
                - \staccato
                e''8
                - \staccato
                ds''8
                - \staccato
                as'8
                - \staccato
                ds''8
                - \staccato
                e''8
                - \staccato
                ds''8
                - \staccato
                c''8
                - \staccato
                ds''8
                - \staccato
                e''8
                - \staccato
                ds''8
                - \staccato
                as'8
                - \staccato
                ds''8
                - \staccato
                e''8
                - \staccato
                ds''8
                - \staccato
                as'8
                - \staccato
                ds''8
                - \staccato
                e''8
                - \staccato
                ds''8
                - \staccato
                c''8
                - \staccato
                ds''8
                - \staccato
                e''8
                - \staccato
                ds''8
                - \staccato
                r2
                <c'' ds'' e''>2
                :32
                \p
                \<
                ~
                <c'' ds'' e''>1
                :32
                :32
                r8
                cs'8
                \mf
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
                fs'8
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
                r4
                <c' df' gf'>4
                :32
                \p
                \<
                ~
                <c' df' gf'>2
                :32
                :32
                r8
                \f
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
                r4
                <c' gf'>4
                :32
                \p
                \<
                ~
                <c' gf'>2
                :32
                :32
                r8
                \f
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
                <e' e''>1
                <fs' b' c''>4
                \f
                - \accent
                - \staccato
                r4
                r8
                b''8
                - \staccato
                b''16
                - \staccato
                c'''16
                - \staccato
                c'''8
                - \staccato
                - \accent
                r8
                - \staccato
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
                r4
                <gs'' cs''' d'''>4
                :32
                \p
                \<
                ~
                <gs'' cs''' d'''>2
                :32
                ~
                <gs'' cs''' d'''>1
                :32
                :32
                r8
                - \staccato
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
                \sfz
                - \staccato
                - \accent
                ^ \markup { * }
                ^ \markup { with the pedal }
                ^ \markup { the tail of the sound }
                ^ \markup { try to capture only }
                r2
                <d'' af''>1
                :32
                :32
                \fermata
                \ppp
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
                e'1
                ~
                \sustainOn
                e'1
                e'8
                - \staccato
                \sustainOff
                r8
                r4
                r2
                R1
                R1
                r2
                e'2
                ~
                \sustainOn
                e'1
                <
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
                \sfz
                - \staccato
                - \accent
                _ \markup { * forearm on keys }
                \sustainOff
                r4
                r2
                r2
                r4
                <e, e>4
                - \staccato
                - \accent
                R1
                r2
                r4
                r8
                <
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
                \sfz
                - \staccato
                - \accent
                _ \markup { * }
                r4
                gf4
                ~
                \sustainOn
                gf2
                gf8
                - \staccato
                \sustainOff
                r8
                r4
                r4
                <e,, e,>4
                - \staccato
                - \accent
                r4
                <gf,, gf,>4
                - \staccato
                - \accent
                r2
                <
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
                \sfz
                - \staccato
                - \accent
                _ \markup { * }
                r4
                \sustainOn
                r2
                gf8
                - \staccato
                \sustainOff
                r8
                <bf, gf>4
                - \tenuto
                - \accent
                gf,4
                (
                <d gf>4
                - \staccato
                )
                <ef, ef>1
                r4
                <c af>4
                - \tenuto
                - \accent
                af,4
                (
                <e af>4
                - \staccato
                )
                <f, f>1
                r8
                - \staccato
                <d bf>8
                - \staccato
                bf,8
                - \staccato
                <gf bf>8
                - \staccato
                r8
                - \staccato
                <bf, g>8
                - \staccato
                g,8
                - \staccato
                <e g>8
                - \staccato
                r8
                - \staccato
                <e c'>8
                - \staccato
                c8
                - \staccato
                <gs c'>8
                - \staccato
                <b, b>2
                <d, d>4
                - \accent
                - \staccato
                r4
                d,4
                (
                <as, d>4
                - \staccato
                )
                r4
                d4
                ~
                \sustainOn
                d2
                ~
                d1
                d4
                - \staccato
                \sustainOff
                <d, d>4
                - \accent
                - \staccato
                r4
                <d, d>4
                - \accent
                - \staccato
                ds,8
                - \staccato
                e8
                - \staccato
                ds,8
                - \staccato
                e8
                - \staccato
                ds,8
                - \staccato
                e8
                - \staccato
                ds,8
                - \staccato
                e8
                - \staccato
                r4
                <e,, e,>4
                - \accent
                - \staccato
                ds,,8
                - \staccato
                e,8
                - \staccato
                ds,,8
                - \staccato
                e,8
                - \staccato
                f,,8
                - \staccato
                gf,8
                - \staccato
                f,,8
                - \staccato
                gf,8
                - \staccato
                f,,8
                - \staccato
                gf,8
                - \staccato
                f,,8
                - \staccato
                gf,8
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
                \sfz
                - \staccato
                - \accent
                _ \markup { * }
                \sustainOn
                r2
                R1
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}