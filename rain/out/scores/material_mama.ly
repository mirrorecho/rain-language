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
        }
        \context StaffGroup = ""
        <<
            \context Staff = "Piano 1"
            {
                ef'4
                e'4
                fs'4
                e'4
            }
            \context Staff = "Piano 2"
            {
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}