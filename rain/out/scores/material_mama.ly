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
            af'4
            - \accent
            \<
            ~
            \ottava -1
            af'2
            :16
            \longfermata
            - \tenuto
            (
            \(
            b'4
            - \staccato
            )
            \bar "||"
            c''2
            \p
            - \tenuto
            b'4
            \)
            \ottava 0
            c'4
            - \accent
            \<
            ~
            \ottava -1
            c'2
            :16
            \longfermata
            - \tenuto
            (
            \(
            ef'4
            - \staccato
            )
            \bar "||"
            e'2
            \p
            - \tenuto
            ef'4
            \)
            \ottava 0
        }
        \context StaffGroup = ""
        <<
            \context Staff = "Piano 1"
            {
                <c' d'>8
                [
                f'8
                ]
                e'8
                [
                g'8
                ]
                <c' d'>4
                [
                f'4
                ]
                e'4
                [
                g'4
                ]
            }
            \context Staff = "Piano 2"
            {
                c4.
                r4
                c4.
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}