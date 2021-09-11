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
            b8
            cs'8
            d'8
            ~
            d'2
            r8
            b8
            cs'8
            d'8
            ~
            d'4
            e'4
            ~
            e'2
            r4
            e'4
            g'4
            ~
            g'8
            f'8
            ~
            f'4
            e'4
            ~
            e'4
            g'4
            f'4
            d'4
            ~
            d'1
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
                ~
                <a d'>4
            }
            \context Staff = "Piano 2"
            {
                \time 4/4
                \clef "bass"
                g,2
                g,2
                g,2
                g,2
                g,2
                g,2
                g,2
                g,2
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}