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
                g''8
                (
                ]
                bf''8
                [
                <a'' a'''>8
                ~
                ]
                <a'' a'''>4
                ~
                <a'' a'''>8
                <c'' c'''>8
                ~
                <c'' c'''>2
                )
                bf4
                bf4
                bf4
                bf4
            }
            \context Staff = "Piano 2"
            {
                \time 4/4
                \clef "bass"
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