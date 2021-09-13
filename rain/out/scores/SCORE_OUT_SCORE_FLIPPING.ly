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
        \with
        {
            accidentalStyle = neo-modern-cautionary
            pedalSustainStyle = #'mixed
        }
        {
            \tempo Angry 4=126
            \time 4/4
            \clef "treble"
            r2
            r8
            cs'''8
            \f
            - \accent
            ~
            cs'''4
            \p
            \<
            cs'''8
            \f
            - \marcato
            - \staccato
            - \accent
            r8
            r4
            r2
            r2
            r4
            r8
            d'''8
            \f
            - \accent
            ~
            d'''1
            \p
            \<
            ~
            d'''8
            d'''8
            \f
            - \marcato
            - \staccato
            - \accent
            r4
            r2
            r2
            r4
            r8
            c'''8
            \f
            - \accent
            ~
            c'''1
            \p
            \<
            c'''8
            \f
            - \marcato
            - \staccato
            - \accent
            r8
            r4
            r4
            r8
            f''8
            - \tenuto
            g'''8
            - \staccato
            - \accent
            af''8
            ~
            af''4
            ~
            af''4
            r4
            r1
            r8
            af''8
            - \tenuto
            b''8.
            - \tenuto
            bf'''16
            - \accent
            - \staccato
            - \marcato
            r2
            r1
            r8
            af''8
            - \tenuto
            b''8.
            - \tenuto
            bf'''16
            - \accent
            - \staccato
            - \marcato
            r8
            df'''8
            \f
            - \accent
            ~
            df'''4
            \p
            \<
            ~
            df'''1
            df'''8
            \f
            - \marcato
            - \staccato
            - \accent
            r8
            r4
            r4
            r8
            df''8
            - \tenuto
            f''8
            - \staccato
            - \accent
            ef''8
            ~
            ef''4
            ~
            ef''2
            r4
            cs'''8
            - \staccato
            - \accent
            - \marcato
            r8
            gs''4
            - \staccato
            - \accent
            fs''4
            - \staccato
            - \accent
            d'''4
            - \staccato
            - \accent
            r8
            cs'''8
            - \staccato
            - \accent
            - \marcato
            r4
            r8
            b''8
            - \tenuto
            d'''8.
            - \tenuto
            cs''''16
            - \accent
            - \staccato
            - \marcato
            r4
            r8
            a'''8
            \f
            - \accent
            ~
            a'''4
            \mf
            \<
            ~
            a'''8
            a'''8
            \ff
            - \marcato
            - \staccato
            - \accent
            r8
            b'''8
            \f
            - \accent
            ~
            b'''4
            \mf
            \<
            ~
            b'''8
            b'''8
            \ff
            - \marcato
            - \staccato
            - \accent
        }
        \context PianoStaff = ""
        <<
            \context Staff = "Piano 1"
            \with
            {
                accidentalStyle = neo-modern-cautionary
                pedalSustainStyle = #'mixed
            }
            {
                \time 4/4
                \clef "treble"
                b'8
                \f
                - \staccato
                d''8
                - \accent
                (
                f''16
                - \staccato
                )
                cs''16
                (
                e''16
                g''16
                - \staccato
                - \accent
                )
                r8
                <b' e'' a''>8
                - \marcato
                r4
                <b' e'' a''>16
                - \marcato
                <b' e'' a''>16
                - \marcato
                r8
                r4
                b'8
                - \staccato
                d''8
                - \accent
                (
                b'8
                - \staccato
                )
                d''8
                - \accent
                (
                b'8
                - \staccato
                )
                d''8
                - \accent
                (
                f''16
                - \staccato
                )
                cs''16
                (
                e''16
                g''16
                - \staccato
                - \accent
                )
                r4
                r8
                <d'' g'' c'''>8
                - \marcato
                r4
                <d'' g'' af''>16
                - \staccato
                r16
                r8
                r2
                <d'' g'' c'''>16
                - \marcato
                <d'' g'' c'''>16
                - \marcato
                <d'' g'' c'''>8
                - \marcato
                r4
                d''8
                - \staccato
                f''8
                - \accent
                (
                d''8
                - \staccato
                )
                f''8
                - \accent
                (
                d''8
                - \staccato
                )
                f''8
                - \accent
                (
                d''8
                - \staccato
                )
                f''8
                - \accent
                (
                af''16
                - \staccato
                )
                e''16
                (
                g''16
                bf''16
                - \staccato
                - \accent
                )
                r8
                <d'' g'' c'''>8
                - \marcato
                r1
                <d'' g'' c'''>16
                - \marcato
                <d'' g'' c'''>16
                - \marcato
                <d'' g'' c'''>16
                - \marcato
                <d'' g'' c'''>16
                - \marcato
                <d'' g'' c'''>16
                - \marcato
                <d'' g'' c'''>16
                - \marcato
                <d'' g'' c'''>16
                - \marcato
                <d'' g'' c'''>16
                - \marcato
                r2
                <d'' g'' af''>16
                - \staccato
                r16
                r8
                r4
                r2
                f''8
                - \staccato
                <g'' af''>8
                - \accent
                (
                f''8
                - \staccato
                )
                <g'' af''>8
                - \accent
                (
                f''8
                - \staccato
                )
                <g'' af''>8
                - \accent
                (
                f''8
                - \staccato
                )
                <g'' af''>8
                - \accent
                (
                f''8
                - \staccato
                )
                af''8
                - \accent
                (
                b''16
                - \staccato
                )
                g''16
                (
                bf''16
                df'''16
                - \staccato
                - \accent
                )
                r4
                f''8
                - \staccato
                <g'' af'' bf''>8
                - \accent
                (
                f''8
                - \staccato
                )
                <g'' af'' bf''>8
                - \accent
                (
                f''8
                - \staccato
                )
                <g'' af'' bf''>8
                - \accent
                (
                f''8
                - \staccato
                )
                <g'' af'' bf''>8
                - \accent
                (
                f''8
                - \staccato
                )
                <g'' af'' bf''>8
                - \accent
                (
                f''8
                - \staccato
                )
                af''8
                - \accent
                (
                b''16
                - \staccato
                )
                g''16
                (
                bf''16
                df'''16
                - \staccato
                - \accent
                )
                r8
                <f'' bf'' ef'''>8
                - \marcato
                r4
                <f'' bf'' ef'''>16
                - \marcato
                <f'' bf'' ef'''>16
                - \marcato
                r8
                r4
                <f'' bf'' ef'''>16
                - \marcato
                <f'' bf'' ef'''>16
                - \marcato
                <f'' bf'' ef'''>16
                - \marcato
                <f'' bf'' ef'''>16
                - \marcato
                r4
                <f'' bf'' ef'''>16
                - \marcato
                <f'' bf'' ef'''>16
                - \marcato
                <f'' bf'' ef'''>16
                - \marcato
                <f'' bf'' ef'''>16
                - \marcato
                <f'' bf'' ef'''>16
                - \marcato
                <f'' bf'' ef'''>16
                - \marcato
                <f'' bf'' ef'''>16
                - \marcato
                <f'' bf'' ef'''>16
                - \marcato
                <f'' bf'' ef'''>16
                - \marcato
                <f'' bf'' ef'''>16
                - \marcato
                <f'' bf'' ef'''>16
                - \marcato
                <f'' bf'' ef'''>16
                - \marcato
                r4
                <f'' as'' b''>16
                - \staccato
                r16
                r8
                r4
                r2
                r4
                <gs'' cs''' fs'''>16
                - \marcato
                <gs'' cs''' fs'''>16
                - \marcato
                r8
                gs''8
                - \staccato
                <as'' b'' cs'''>8
                - \accent
                (
                gs''8
                - \staccato
                )
                b''8
                - \accent
                (
                d'''16
                - \staccato
                )
                as''16
                (
                cs'''16
                e'''16
                - \staccato
                - \accent
                )
                r8
                <gs'' cs''' fs'''>8
                - \marcato
                gs''8
                - \staccato
                <as'' b'' cs'''>8
                - \accent
                (
                gs''8
                - \staccato
                )
                b''8
                - \accent
                (
                d'''16
                - \staccato
                )
                as''16
                (
                cs'''16
                e'''16
                - \staccato
                - \accent
                )
                r4
                r8
                <b'' e''' a'''>8
                - \marcato
                r8
                <b'' e''' a'''>16
                - \marcato
                <b'' e''' a'''>16
                - \marcato
                <b'' e''' a'''>16
                - \marcato
                <b'' e''' a'''>16
                - \marcato
                <b'' e''' a'''>8
                - \marcato
                r8
                <b'' e''' a'''>8
                - \marcato
                r8
                <b'' e''' a'''>8
                - \marcato
                r8
                \ottava 1
                <b''' e'''' a''''>8
                - \marcato
                r4
                <d'''' g'''' c'''''>16
                \ff
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                <d'''' g'''' c'''''>16
                - \marcato
                \bar "|."
                \ottava 0
            }
            \context Staff = "Piano 2"
            \with
            {
                accidentalStyle = neo-modern-cautionary
                pedalSustainStyle = #'mixed
            }
            {
                \clef "treble"
                b8
                - \staccato
                b8
                - \accent
                ~
                b16
                b16
                (
                d'16
                f'16
                - \staccato
                - \accent
                )
                r8
                <f f'>8
                - \marcato
                r4
                <f f'>16
                - \marcato
                <f f'>16
                - \marcato
                r8
                r4
                r8
                b8
                - \accent
                - \tenuto
                r8
                b8
                - \accent
                - \tenuto
                b8
                - \staccato
                b8
                - \accent
                ~
                b16
                b16
                (
                d'16
                f'16
                - \staccato
                - \accent
                )
                r4
                r8
                <af af'>8
                - \marcato
                r4
                r16
                <d' g' af'>16
                - \tenuto
                ~
                <d' g' af'>8
                ~
                <d' g' af'>2
                <af af'>16
                - \marcato
                <af af'>16
                - \marcato
                <af af'>8
                - \marcato
                r4
                r8
                d'8
                - \accent
                - \tenuto
                r8
                d'8
                - \accent
                - \tenuto
                r8
                d'8
                - \accent
                - \tenuto
                d'8
                - \staccato
                d'8
                - \accent
                ~
                d'16
                d'16
                (
                f'16
                af'16
                - \staccato
                - \accent
                )
                r8
                <af af'>8
                - \marcato
                r1
                <af af'>16
                - \marcato
                <af af'>16
                - \marcato
                <af af'>16
                - \marcato
                <af af'>16
                - \marcato
                <af af'>16
                - \marcato
                <af af'>16
                - \marcato
                <af af'>16
                - \marcato
                <af af'>16
                - \marcato
                r2
                r16
                <d' g' af'>16
                - \tenuto
                ~
                <d' g' af'>8
                ~
                <d' g' af'>4
                ~
                <d' g' af'>4
                r4
                r8
                f'8
                - \accent
                - \tenuto
                r8
                f'8
                - \accent
                - \tenuto
                r8
                f'8
                - \accent
                - \tenuto
                r8
                f'8
                - \accent
                - \tenuto
                f'8
                - \staccato
                f'8
                - \accent
                ~
                f'16
                f'16
                (
                af'16
                b'16
                - \staccato
                - \accent
                )
                r4
                r8
                f'8
                - \accent
                - \tenuto
                r8
                f'8
                - \accent
                - \tenuto
                r8
                f'8
                - \accent
                - \tenuto
                r8
                f'8
                - \accent
                - \tenuto
                r8
                f'8
                - \accent
                - \tenuto
                f'8
                - \staccato
                f'8
                - \accent
                ~
                f'16
                f'16
                (
                af'16
                b'16
                - \staccato
                - \accent
                )
                r8
                <b b'>8
                - \marcato
                r4
                <b b'>16
                - \marcato
                <b b'>16
                - \marcato
                r8
                r4
                <b b'>16
                - \marcato
                <b b'>16
                - \marcato
                <b b'>16
                - \marcato
                <b b'>16
                - \marcato
                r4
                <b b'>16
                - \marcato
                <b b'>16
                - \marcato
                <b b'>16
                - \marcato
                <b b'>16
                - \marcato
                <b b'>16
                - \marcato
                <b b'>16
                - \marcato
                <b b'>16
                - \marcato
                <b b'>16
                - \marcato
                <b b'>16
                - \marcato
                <b b'>16
                - \marcato
                <b b'>16
                - \marcato
                <b b'>16
                - \marcato
                r4
                r16
                <f' as' b'>16
                - \tenuto
                ~
                <f' as' b'>8
                ~
                <f' as' b'>4
                ~
                <f' as' b'>2
                r4
                <d' d''>16
                - \marcato
                <d' d''>16
                - \marcato
                r8
                r8
                gs'8
                - \accent
                - \tenuto
                gs'8
                - \staccato
                gs'8
                - \accent
                ~
                gs'16
                gs'16
                (
                b'16
                d''16
                - \staccato
                - \accent
                )
                r8
                <d' d''>8
                - \marcato
                r8
                gs'8
                - \accent
                - \tenuto
                gs'8
                - \staccato
                gs'8
                - \accent
                ~
                gs'16
                gs'16
                (
                b'16
                d''16
                - \staccato
                - \accent
                )
                r4
                r8
                <f' f''>8
                - \marcato
                r8
                <f' f''>16
                - \marcato
                <f' f''>16
                - \marcato
                <f' f''>16
                - \marcato
                <f' f''>16
                - \marcato
                <f' f''>8
                - \marcato
                r8
                <f' f''>8
                - \marcato
                r8
                <f' f''>8
                - \marcato
                r8
                <f'' f'''>8
                - \marcato
                r4
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
                <af'' af'''>16
                - \marcato
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}