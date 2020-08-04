from altium_to_quartus import parse_args

def test_default_args():
    input_file_name, output_file_name, ref_des = parse_args('program_name', 'input_name.net')
    assert input_file_name == 'input_name.net'
    assert output_file_name == 'input_name.qsf'
    assert ref_des == 'U1'