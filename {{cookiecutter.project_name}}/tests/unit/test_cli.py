from typer.testing import CliRunner

from {{ cookiecutter.package_name }}.cli import app

runner = CliRunner(mix_stderr=False)


{% if cookiecutter.commands == "single" %}
def test_command(mocker):
    m = mocker.patch("{{ cookiecutter.package_name }}.{{ cookiecutter.package_name }}.answer_everything", return_value=5)

    result = runner.invoke(app)

    m.assert_called_once()
    assert result.exit_code == 0
    assert result.stdout == "5\n"
{% endif %}

{% if cookiecutter.commands == "multiple" %}
def test_start_command():
    result = runner.invoke(app, ["start"])

    assert result.exit_code == 0
    assert result.stdout == "{{cookiecutter.project_title}} started\n"


def test_answer_command(mocker):
    m = mocker.patch("{{ cookiecutter.package_name }}.{{ cookiecutter.package_name }}.answer_everything", return_value=5)

    result = runner.invoke(app, ["answer"])

    m.assert_called_once()
    assert result.exit_code == 0
    assert result.stdout == "5\n"
{% endif %}