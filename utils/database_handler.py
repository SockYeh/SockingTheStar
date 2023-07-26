from decouple import config
from supabase import create_client, Client
from secrets import token_hex

url: str = config("SUPABASE_URL")
key: str = config("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def get_user_by_email(email: str) -> dict:
    """Fetches a user from the database by their email."""
    return supabase.table("auth_db").select("*").eq("email", email).execute().data[0]


def get_user_by_id(user_id: str) -> dict:
    """Fetches a user from the database by their ID."""
    return supabase.table("auth_db").select("*").eq("id", user_id).execute().data[0]


def create_user(email: str, username: str, password: str) -> dict:
    """Creates a user in the database."""
    return (
        supabase.table("auth_db")
        .insert(
            {
                "email": email,
                "username": username,
                "password": password,
                "api_key": token_hex(32),
            }
        )
        .execute()
    ).data[0]


def fetch_api_key(user_id: str) -> str:
    """Fetches the API key of a user from the database."""
    return (
        supabase.table("auth_db").select("api_key").eq("id", user_id).execute()
    ).data[0]["api_key"]
