import os, subprocess, sys
def run(cmd):
    assert subprocess.call(cmd, shell=True) == 0
def test_make_intro(tmp_path):
    out = tmp_path/"intro.md"
    run(f'{sys.executable} academic_writing_agent.py --title "X" --template intro --outfile "{out}"')
    assert out.exists()
    txt = out.read_text(encoding="utf-8")
    for h in ["Known facts", "Brief subject review", "Research gap", "This study"]:
        assert h.split()[0] in txt
