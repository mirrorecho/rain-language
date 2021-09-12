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
        \context PianoStaff = ""
        <<
            \context Staff = "Piano 1"
            {
                \tempo Angry 4=132
                \time 4/4
                \clef "treble"
                bf'8
                \f
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
                - \marcato
                r4
                <bf' ef'' af''>16
                - \marcato
                <bf' ef'' af''>16
                - \marcato
                r8
                r4
                bf'8
                - \staccato
                cs''8
                - \accent
                (
                bf'8
                - \staccato
                )
                cs''8
                - \accent
                (
                bf'8
                - \staccato
                )
                cs''8
                - \accent
                (
                e''16
                - \staccato
                )
                c''16
                (
                ef''16
                fs''16
                - \staccato
                - \accent
                )
            }
            \context Staff = "Piano 2"
            {
                \time 4/4
                \clef "bass"
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
                r8
                <e e'>8
                - \marcato
                r4
                <e e'>16
                - \marcato
                <e e'>16
                - \marcato
                r8
                r4
                bf8
                - \staccato
                bf8
                - \accent
                bf8
                - \staccato
                bf8
                - \accent
                bf8
                - \staccato
                bf8
                - \accent
                ~
                bf16
                bf16
                (
                cs'16
                e'16
                - \staccato
                - \accent
                )
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}