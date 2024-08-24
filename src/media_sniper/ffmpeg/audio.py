import os
import subprocess

_output_filename_prefix = "merged"
_audio_merge_list_filename = "audio_merge_list.txt"


def merge(clips: [], output_folder: str, file_type=".mp3"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_filename = _output_filename_prefix + file_type
    output_filepath = os.path.join(output_folder, output_filename)
    output_merge_list_filepath = os.path.join(output_folder, _audio_merge_list_filename)

    # Step 1: Check if the output file exists. If so, delete it for overwriting.
    if os.path.isfile(output_filepath) is True:
        os.remove(output_filepath)

    # Step 2: Write media list to a TXT file.
    with open(output_merge_list_filepath, "w") as ff:
        for clip in clips:
            content = "file {}\n".format(clip)
            ff.write(content)

    # Step 3: Merge media clips with FFMpeg command.

    # $ ffmpeg -f concat -i media_list.txt out.mpn
    # 'media_list.txt' - It contains the path of each media clip.
    # Note:
    #     The path of one clip is 'media_clips/media_clip_1.mpn'.
    #     It has the same parent folder 'PATH_MEDIA' as 'media_list.txt'.
    # Note:
    #     Removing 'copy' re-encodes clips and avoids black screen/frames.
    #     Removing 'copy' leads to high CPU load and long operating time.
    # Generate the command for processing input media.
    cmd = "ffmpeg -f concat -safe 0 -i {}  {}".format(
        output_merge_list_filepath, output_filepath
    )

    print("cmd content: ", cmd)

    # Execute the (Terminal) command within Python.
    subprocess.call(cmd, shell=True)
