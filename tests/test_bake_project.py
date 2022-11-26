def test_bake_project_default_single_commands(cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()


def test_bake_project_multiple_commands(cookies):
    result = cookies.bake(extra_context={"commands": "multiple"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()
