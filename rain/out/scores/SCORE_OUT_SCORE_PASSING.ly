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
            \tempo Dreamy 4.=92
            \time 6/8
            \clef "treble"
            cs'''2.
            \p
            \<
            ~
            (
            cs'''8
            gs''8
            fs''8
            e''8
            ds''4
            \mp
            )
            r2.
            r4.
            as''4.
            \p
            \<
            ~
            (
            as''8
            \mp
            gs''8
            fs''8
            e''8
            ds''8
            )
            gs''8
            (
            fs''8
            e''8
            ds''8
            )
            e''8
            (
            ds''4
            )
            r2.
            bf''8
            \>
            (
            f''8
            ef''8
            df''8
            c''8
            )
            f''8
            (
            ef''8
            df''8
            c''8
            )
            ef''8
            (
            df''8
            c''8
            \p
            )
            r4.
            r8
            r8
            c''8
            \<
            (
            df''8
            c''8
            g''8
            ~
            g''8
            )
            a''4
            \mp
            ~
            a''2.
            \fermata
            \tempo "Freely, Slowing Down" 4.=54
            r4
            g''8
            \>
            (
            d''8
            c''8
            bf'8
            ~
            bf'8
            )
            r8
            d''4
            \fermata
            (
            c''8
            bf'8
            a'4
            \fermata
            )
            r4
            bf'4
            (
            a'2.
            \fermata
            \pp
            )
            \bar "|."
        }
        \context PianoStaff = ""
        <<
            \context Staff = "Piano 1"
            {
                \time 6/8
                \clef "treble"
                r2.
                r4.
                r8
                r8
                gs'8
                \p
                \<
                (
                fs''8
                e''8
                ds''8
                fs''8
                e''8
                ds''8
                \mp
                )
                e''8
                (
                ds''8
                as'8
                ~
                as'8
                )
                <c'' df''>4
                ~
                <c'' df''>2.
                <bf ef' gf'>4.
                \pp
                ~
                <bf ef' gf'>4
                c''8
                \mp
                (
                df''8
                ef''8
                bf'8
                ~
                bf'8
                )
                <c'' df''>4
                ~
                <c'' df''>2.
                <g c' ef'>4.
                ~
                <g c' ef'>4
                c'8
                (
                df'8
                ef'8
                bf'8
                ~
                bf'8
                )
                <c'' df''>4
                <g' c'' df''>4.
                ~
                <g' c'' df''>8
                <g' bf' c'' f''>4
                <a'' bf''>2.
                \fermata
                <e' a' c''>2.
                \pp
                ~
                <e' a' c''>4.
                \fermata
                <e' g' a' d''>4.
                ~
                <e' g' a' d''>4.
                \fermata
                \clef "bass"
                <e a bf>4.
                ~
                <e a bf>2.
                \fermata
            }
            \context Staff = "Piano 2"
            {
                \time 6/8
                \clef "bass"
                r2.
                r2.
                \clef "treble"
                <as ds' fs'>2.
                <as ds' e'>4.
                ~
                <as ds' e'>8
                <bf df' ef' af'>4
                \clef "bass"
                ef,,2.
                \pp
                ~
                ef,,2.
                \clef "treble"
                <bf df' ef'>4.
                ~
                <bf df' ef'>8
                <bf df' ef' af'>4
                \clef "bass"
                ef,,2.
                c,2.
                ~
                c,2.
                <c g>4.
                ~
                <c g>8
                <c a>4
                c,2.
                \fermata
                ~
                c,4.
                a,4.
                ~
                a,2.
                \fermata
                ~
                a,4
                bf,2
                \fermata
                r4
                \fermata
                \ottava -1
                a,,,2
                ^ \fff
                \fermata
                \bar "|."
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}