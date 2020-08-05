from altium_to_quartus import parse_args

def test_default_args():
    input_file_name, output_file_name, ref_des = parse_args('program_name', 'input_name.net')
    assert input_file_name == 'input_name.net'
    assert output_file_name == 'input_name.qsf'
    assert ref_des == 'U1'

def test_specyfic_ref_des():
    input_file_name, output_file_name, ref_des = parse_args('program_name', '-u', 'U7', 'input_name.net')
    assert input_file_name == 'input_name.net'
    assert output_file_name == 'input_name.qsf'
    assert ref_des == 'U7'

def test_specyfic_output_filename():
    input_file_name, output_file_name, ref_des = parse_args('program_name', '-o', 'output_name.sqf', 'input_name.net')
    assert input_file_name == 'input_name.net'
    assert output_file_name == 'output_name.sqf'
    assert ref_des == 'U1'

def test_specyfic_ref_des_and_output_name():
    input_file_name, output_file_name, ref_des = parse_args('program_name', '-u', 'U9', '-o', 'output_name.sqf', 'input_name.net')
    assert input_file_name == 'input_name.net'
    assert output_file_name == 'output_name.sqf'
    assert ref_des == 'U9'

def test_specyfic_ref_des_and_output_name_reversed():
    input_file_name, output_file_name, ref_des = parse_args('program_name', '-o', 'output_name.sqf', '-u', 'U9', 'input_name.net')
    assert input_file_name == 'input_name.net'
    assert output_file_name == 'output_name.sqf'
    assert ref_des == 'U9'