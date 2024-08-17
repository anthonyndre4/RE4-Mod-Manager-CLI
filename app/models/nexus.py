from pydantic import BaseModel


class Category(BaseModel):
    category_id: int
    name: str
    parent_category: bool


class Game(BaseModel):
    id: int
    name: str
    forum_url: str
    nexusmods_url: str
    genre: str
    file_count: int
    downloads: int
    domain_name: str
    approved_date: int
    file_views: int
    authors: int
    file_endorsements: int
    mods: int
    categories: list[Category]
