from datetime import datetime
from pydantic import BaseModel


class Category(BaseModel):
    category_id: int
    name: str
    parent_category: bool | int


class User(BaseModel):
    member_id: int
    member_group_id: int
    name: str


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


class LatestMods(BaseModel):
    name: str | None
    summary: str | None
    description: str | None
    picture_url: str | None
    mod_downloads: int | None
    mod_unique_downloads: int | None
    uid: int
    mod_id: int
    game_id: int
    allow_rating: bool
    domain_name: str
    category_id: int
    version: str
    endorsement_count: int
    created_timestamp: int
    created_time: datetime
    updated_timestamp: int
    updated_time: datetime
    author: str
    uploaded_by: str
    uploaded_users_profile_url: str
    contains_adult_content: bool
    status: str
    available: bool
    user: User
    endorsement: str | None
