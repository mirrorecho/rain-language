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
                \time 4/4
                \clef "treble"
                <ef' d''>8
                \mf
                c''8
                <g' f''>8
                af'8
                <f' e''>8
                bf'8
                <df' c''>8
                bf'8
                <f' ef''>8
                <gf' f''>8
                <ef' d''>8
                <bf' af''>8
                <b as'>8
                <gs g'>8
                <ds' cs''>8
                <e' ds''>8
                <cs' c''>8
                <gs' fs''>8
                f'8
                <a gs'>8
                <fs f'>8
                <cs' b'>8
                as8
            }
            \context Staff = "Piano 2"
            {
                \time 4/4
                \clef "bass"
                g8
                f8
                bf8
                c'8
                bf8
                ef8
                f8
                ef8
                af8
                bf8
                af8
                df'8
                ds8
                cs8
                fs8
                gs8
                fs8
                fs8
                b8
                cs8
                b,8
                b,8
                e8
            }
        >>
    >>
%! abjad.LilyPondFile._get_formatted_blocks()
}