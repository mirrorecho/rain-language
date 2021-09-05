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
            af1
            fs1
            b1
            cs'1
            b1
            e'1
            fs'1
            e'1
            a'1
        }
        \context StaffGroup = ""
        <<
            \context Staff = "Piano 1"
            {
                \time 4/4
                <e' ef''>8
                <cs' c''>8
                <af' fs''>8
                r8
                r2
                r1
                r1
                <a' af''>8
                <fs' f''>8
                <cs'' b''>8
                r8
                r2
                r1
                r1
                <d'' cs'''>8
                <b' bf''>8
                <fs'' e'''>8
                r8
                r2
                r1
                r1
                <g' fs''>4
                - \accent
                <e' ef''>4
                <b' a''>4
                af'4
                <c'' b''>8
                <a' af''>8
                <e'' d'''>8
                cs''8
            }
            \context Staff = "Piano 2"
            {
                \time 4/4
                r1
                r1
                r1
                r1
                r1
                r1
                r1
                r1
                r1
                b8
                a8
                a8
                d'8
                r2
                e'8
                d'8
                d'8
                g'8
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}