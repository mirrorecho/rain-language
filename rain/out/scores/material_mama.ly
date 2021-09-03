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
                \time 4/4
                <e' ef''>8
                <cs' c''>8
                <af' fs''>8
                <a' af''>8
                <fs' f''>8
                <cs'' b''>8
                <d'' cs'''>8
                <b' bf''>8
                <fs'' e'''>8
                <g' fs''>8
                <e' ef''>8
                <b' a''>8
                af'8
                <c'' b''>8
                <a' af''>8
                <e'' d'''>8
                cs''8
            }
            \context Staff = "Piano 2"
            {
                \time 4/4
                af8
                fs8
                b8
                cs'8
                b8
                e'8
                fs'8
                e'8
                a'8
                b8
                a8
                a8
                d'8
                e'8
                d'8
                d'8
                g'8
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}