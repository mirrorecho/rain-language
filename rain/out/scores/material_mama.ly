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
                bf8
                ef'8
                e'8
                ef'8
                c'8
                ef'8
                e'8
                ef'8
                c'8
                cs'8
                e'8
                cs'8
                c'8
                cs'8
                fs'8
                cs'8
                c'8
                f'8
                fs'8
                f'8
                d'8
                f'8
                fs'8
                f'8
                d'8
                ef'8
                fs'8
                ef'8
                d'8
                ef'8
                af'8
                ef'8
            }
            \context Staff = "Piano 2"
            {
                \clef "bass"
                e,4
                (
                <af, e>4
                )
                e,4
                (
                <c e>4
                )
                cs,4
                (
                <e, cs>4
                )
                cs,4
                (
                <bf, cs>4
                )
                \clef "bass"
                fs,4
                (
                <bf, fs>4
                )
                fs,4
                (
                <d fs>4
                )
                ef,4
                (
                <fs, ef>4
                )
                ef,4
                (
                <c ef>4
                )
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}