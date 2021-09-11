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
            b'8
            (
            cs''8
            d''8
            ~
            d''2
            )
            r1
            r1
            r8
            b'8
            (
            cs''8
            d''8
            ~
            d''2
            )
            r8
            b'8
            (
            cs''8
            d''8
            ~
            d''4
            e''4
            ~
            e''2
            )
            r2
            r8
            b'8
            (
            cs''8
            d''8
            ~
            d''2
            )
            r8
            b'8
            (
            cs''8
            d''8
            ~
            d''4
            e''4
            ~
            e''2
            )
            r4
            e''4
            (
            g''4
            ~
            g''8
            f''8
            ~
            f''4
            e''4
            ~
            e''8
            )
            r8
            r4
            r2
            r8
            d''8
            (
            e''8
            f''8
            ~
            f''2
            )
            r8
            d''8
            (
            e''8
            f''8
            ~
            f''4
            g''4
            ~
            g''2
            )
            r4
            g''4
            (
            bf''4
            ~
            bf''8
            af''8
            ~
            af''4
            g''4
            ~
            g''8
            )
            r8
            bf''4
            (
            f''4
            bf''4
            ~
            bf''1
            )
        }
        \context PianoStaff = ""
        <<
            \context Staff = "Piano 1"
            {
                \time 4/4
                \clef "treble"
                r4
                <a d'>4
                ~
                <a d'>4
                <b d'>4
                ~
                <b d'>4
                <cs' d'>4
                ~
                <cs' d'>4
                <d' e'>4
                ~
                <d' e'>4
                <d' g'>4
                ~
                <d' g'>4
                <g f'>4
                ~
                <g f'>4
                <d' e'>4
                ~
                <d' e'>4
                <a d'>4
                r4
                <a d'>4
                ~
                <a d'>4
                <b d'>4
                ~
                <b d'>4
                <cs' d'>4
                ~
                <cs' d'>2
                r1
                r4
                <a d'>4
                ~
                <a d'>4
                <b d'>4
                ~
                <b d'>4
                <cs' d'>4
                ~
                <cs' d'>2
                <d' e'>2
                <d' g'>2
                <g f'>2
                r2
                r4
                <cs' d'>4
                ~
                <cs' d'>4
                <d' e'>4
                ~
                <d' e'>4
                <d' g'>4
                ~
                <d' g'>2
                <g f'>2
                <d' e'>2
                <a d'>1
                ~
                <a d'>4
                r4
                r2
                r4
                <a' d''>4
                ~
                <a' d''>4
                <d'' f''>4
                ~
                <d'' f''>4
                <e'' f''>4
                ~
                <e'' f''>4
                <f'' g''>4
                ~
                <f'' g''>4
                <f'' bf''>4
                ~
                <f'' bf''>2
                <bf' af''>2
                <f'' g''>2
                <c'' f''>1
                <c'' ef'' f''>1
                r8
                g'8
                (
                a'8
                bf'8
                ~
                bf'4
                c''4
                ~
                c''2
                )
            }
            \context Staff = "Piano 2"
            {
                \time 4/4
                \clef "bass"
                g,1
                g,1
                g,1
                g,2
                g,2
                g,1
                g,1
                r1
                g,1
                g,2
                g,2
                g,2
                g,2
                g,2
                r2
                r2
                g,2
                g,2
                g,2
                g,1
                g,2
                g,2
                ~
                g,4
                r4
                r2
                r2
                <g, d>2
                g,2
                f,2
                d,2
                <c, af,>2
                bf,,2
                <bf,, f,>2
                bf,,2
                <bf,, f,>2
                bf,,2
                <bf,, f,>2
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}