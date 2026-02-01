from mcp.server.fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("auto-paper-reviewer")

CHECKLIST_PATH = Path("checklist.txt")

_cached_paper = None
_cached_path = None


def read(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8")


# Aishwarya Gadhave
@mcp.tool()
def load_paper(paper_path: str) -> dict:
    """
    Load paper from user provided txt file path.
    Example: "paper.txt" or "./papers/sample.txt"
    """
    global _cached_paper, _cached_path

    path = Path(paper_path)
    _cached_paper = read(path)
    _cached_path = str(path)

    return {
        "paper_loaded": True,
        "file": _cached_path,
        "length": len(_cached_paper),
    }


# Aishwarya Gadhave
@mcp.tool()
def find_missing_citations() -> dict:
    if _cached_paper is None:
        raise RuntimeError("paper_not_loaded")

    return {
        "task": "citations",
        "source_file": _cached_path,
        "paper": _cached_paper,
        "checks": [
            "unsupported_claims",
            "missing_related_work",
            "outdated_references"
        ]
    }


# Aishwarya Gadhave
@mcp.tool()
def detect_logical_gaps() -> dict:
    if _cached_paper is None:
        raise RuntimeError("paper_not_loaded")

    return {
        "task": "logic",
        "source_file": _cached_path,
        "paper": _cached_paper,
        "checks": [
            "assumption_gaps",
            "missing_proofs",
            "unclear_methodology",
            "invalid_inference"
        ]
    }


# Vishwajeet Godse
@mcp.tool()
def get_article_statistics(articles: list[dict]) -> dict:
    """
    Returns total number of articles and category-wise article counts.
    Each article must contain:
    - title (string)
    - category (string)
    """

    total_articles = len(articles)
    category_counts = {}

    for article in articles:
        category = article.get("category", "Unknown")
        category_counts[category] = category_counts.get(category, 0) + 1

    return {
        "total_articles": total_articles,
        "category_counts": category_counts
    }


if __name__ == "__main__":
    mcp.run()
