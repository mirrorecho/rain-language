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
                bf'8
                - \staccato
                df''8
                - \accent
                (
                e''16
                - \staccato
                )
                c''16
                (
                ef''16
                gf''16
                - \staccato
                - \accent
                )
                r8
                <bf' ef'' af''>8
                - \accent
                r4
                <bf' ef'' af''>16
                - \accent
                <bf' ef'' af''>16
                - \accent
                r8
                r4
                bf'8
                - \staccato
                df''8
                - \accent
                (
                e''16
                - \staccato
                )
                c''16
                (
                ef''16
                gf''16
                - \staccato
                - \accent
                )
            }
            \context Staff = "Piano 2"
            {
                \time 4/4
                bf8
                - \staccato
                bf8
                - \accent
                ~
                bf16
                bf16
                (
                df'16
                e'16
                - \staccato
                - \accent
                )
                r2
                r2
                bf8
                - \staccato
                bf8
                - \accent
                ~
                bf16
                bf16
                (
                df'16
                e'16
                - \staccato
                - \accent
                )
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}