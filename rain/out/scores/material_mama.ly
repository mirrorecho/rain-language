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
                g'8
                d'8
                c'8
                bf8
                a8
                d'8
                c'8
                bf8
                a8
                c'8
                bf8
                a8
                bf8
                a8
                e8
                ~
                e8
                <fs g>8
                ~
                <fs g>8
                ~
                <fs g>2.
                e'8
                d'8
                c'8
                bf8
                a8
                d'8
                c'8
                bf8
                a8
                bf8
                a4
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
                r2.
                r2.
                r2.
                r2.
                r2.
                r2.
                r2.
                cs'8
                b8
                a8
                g8
                fs8
                b8
                a8
                g8
                fs8
                g8
                fs4
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}