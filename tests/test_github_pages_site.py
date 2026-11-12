from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_github_pages_static_site_files_exist() -> None:
    required = [
        ROOT / "site" / "index.html",
        ROOT / "site" / "styles.css",
        ROOT / "site" / "app.js",
        ROOT / "site" / "assets" / "github_hero.png",
        ROOT / "site" / "assets" / "pipeline_flow.gif",
        ROOT / "site" / "assets" / "dashboard_preview.png",
    ]
    missing = [str(path) for path in required if not path.exists()]
    assert not missing
    assert all(path.stat().st_size > 1000 for path in required if path.suffix in {".png", ".gif"})


def test_github_pages_workflow_publishes_site_directory() -> None:
    workflow = (ROOT / ".github" / "workflows" / "pages.yml").read_text(encoding="utf-8")
    assert "actions/upload-pages-artifact" in workflow
    assert "actions/deploy-pages" in workflow
    assert "path: site" in workflow
    assert "pages: write" in workflow
    assert "id-token: write" in workflow


def test_pages_site_is_self_contained_static_demo() -> None:
    html = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
    js = (ROOT / "site" / "app.js").read_text(encoding="utf-8")
    assert 'href="styles.css"' in html
    assert 'src="app.js"' in html
    assert "companySelect" in html
    assert "buildPacket" in js
    assert "Static GitHub Pages simulator" in js

