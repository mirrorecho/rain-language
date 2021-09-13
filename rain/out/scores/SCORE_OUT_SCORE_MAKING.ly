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
            \tempo Intense 4=96
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
            R1
            gs''1
            \p
            \<
            d'''8.
            \mf
            b''16
            ~
            b''8
            d'''8
            b''8
            d'''8
            r4
            r4
            ef'''4
            - \tenuto
            bf''4
            - \tenuto
            gf''4
            - \tenuto
            R1
            af''1
            \p
            \<
            f''8.
            \mf
            af''16
            ~
            af''8
            f''8
            af''8
            f''8
            r4
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
            R1
            R1
            R1
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
            r8.
            - \tenuto
            r16
            - \tenuto
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
            R1
            R1
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
            b''8
            - \tenuto
            [
            b''8
            - \tenuto
            ]
            b''8
            - \tenuto
            - \accent
            [
            b''8
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
                ef''8.
                \p
                (
                c''16
                ~
                c''8
                )
                a''8
                ~
                (
                a''16
                c''8.
                )
                f''16
                (
                ef''8.
                )
                d''8.
                (
                c''16
                ~
                c''8
                )
                ef''8
                ~
                (
                ef''16
                c''8.
                )
                f''16
                (
                g''8.
                )
                g''8.
                g''16
                ~
                g''8
                g''8
                ~
                g''16
                g''8.
                g''16
                (
                f''8.
                )
                c''8.
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
                a''16
                ~
                a''8
                )
                c''8
                ~
                (
                c''16
                a''8.
                )
                d'''16
                (
                e'''8.
                )
                e'''8.
                \<
                e'''16
                ~
                e'''8
                e'''8
                ~
                e'''16
                e'''8.
                e'''16
                (
                d'''8.
                )
                gs''1
                \mf
                r4
                \clef "bass"
                <ef gf bf>4
                ~
                <ef gf bf>2
                ef8
                (
                [
                gf8
                ]
                ef8
                [
                gf8
                )
                ]
                f8
                (
                [
                af8
                ]
                f8
                [
                af8
                )
                ]
                gf8
                (
                [
                bf8
                ]
                gf8
                [
                bf8
                )
                ]
                af8
                (
                [
                c'8
                )
                ]
                bf8
                (
                [
                d'8
                ]
                bf8
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
                - \tenuto
                r8
                [
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
                r4
                g'8
                (
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
                c8
                (
                [
                ef8
                ]
                c8
                [
                ef8
                )
                ]
                d8
                (
                [
                f8
                ]
                d8
                [
                f8
                )
                ]
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
                \clef "treble"
                c'8
                (
                [
                e'8
                ]
                c'8
                [
                e'8
                )
                ]
                d'8
                (
                [
                fs'8
                ]
                d'8
                [
                fs'8
                )
                ]
                e'8
                (
                [
                gs'8
                ]
                e'8
                [
                gs'8
                )
                ]
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
                ]
                gs'8
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
                <e' e''>1
                \clef "bass"
                <ef,, ef,>1
                ef,8
                (
                [
                gf,8
                ]
                ef,8
                [
                gf,8
                )
                ]
                f,8
                (
                [
                af,8
                ]
                f,8
                [
                af,8
                )
                ]
                gf,8
                (
                [
                bf,8
                ]
                gf,8
                [
                bf,8
                )
                ]
                af,8
                (
                [
                c8
                )
                ]
                bf,8
                (
                [
                d8
                ]
                bf,8
                [
                d8
                )
                ]
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
                ]
                d8
                [
                f8
                )
                ]
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
                [
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
                r4
                g,8
                (
                [
                b,8
                )
                ]
                a,8
                (
                [
                c8
                )
                ]
                b,8
                (
                [
                d8
                )
                ]
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