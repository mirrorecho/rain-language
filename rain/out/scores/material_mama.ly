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
            r8
            bf8
            c'8
            cs'8
            ~
            cs'2
            r8
            bf8
            c'8
            cs'8
            ~
            cs'4
            ef'4
            ~
            ef'2
            r4
            ef'4
            fs'4
            ~
            fs'8
            e'8
            ~
            e'4
            ef'4
            ~
            ef'4
            fs'4
            e'4
            cs'4
            ~
            cs'1
        }
        \context StaffGroup = ""
        <<
            \context Staff = "Piano 1"
            {
            }
            \context Staff = "Piano 2"
            {
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}