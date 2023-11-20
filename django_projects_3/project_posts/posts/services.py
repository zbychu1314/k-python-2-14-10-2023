from abc import ABC, abstractclassmethod
from dataclasses import dataclass
from .models import Post as ModelPost
from faker import Faker
from datetime import datetime

faker = Faker()

class PostNotFound(Exception):
    pass


@dataclass
class PostsDTO:  # DTO - data transfer object
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_django_model(cls, m: ModelPost) -> 'PostsDTO':
        return PostsDTO(
            id = m.id,
            title=m.title,
            content=m.content,
            created_at=m.created_at,
            updated_at=m.updated_at
        )

class IPostService(ABC):

    @abstractclassmethod
    def list(cls) -> list[PostsDTO]:
        pass

    @abstractclassmethod
    def create(cls, title: str, content: str, created_at: datetime, updated_at: datetime) -> PostsDTO:
        pass
    
    @abstractclassmethod
    def get(cls, id: int) -> PostsDTO:
        pass

class PostService(IPostService):

    @classmethod
    def list(cls) -> list[PostsDTO]:
        posts: list[PostsDTO] = [PostsDTO.from_django_model(m) for m in ModelPost.objects.all()]
        return posts
    

    @classmethod
    def create(cls, title: str, content: str, created_at: datetime, updated_at: datetime) -> PostsDTO:
    
        m = ModelPost.objects.create(
            title=title,
            content=content,
            created_at=created_at,
            updated_at = updated_at

        )

        return PostsDTO.from_django_model(m)
    

    @classmethod
    def get(cls, id: int) -> PostsDTO:
        try:
           return PostsDTO.from_django_model(ModelPost.objects.get(id=id))
        except ModelPost.DoesNotExist:
            pass
        
        
        raise PostNotFound

class FakePostService(IPostService):
    id = 1

    @classmethod
    def list(cls) -> list[PostsDTO]:
        
        p = []
        for i in range(1, 26):
            p.append(
       
                PostsDTO(
                    id=i,
                    title = faker.word(),
                    content=faker.text(),
                    created_at=faker.date_time(),
                    updated_at=faker.date_time()
                )
            )
        
    
        return p
    
    
    @classmethod
    def create(cls, title: str, content: str, created_at: datetime, updated_at: datetime) -> PostsDTO:

        m = PostsDTO(
            id=1,
            title=title,
            content=content,
            created_at=created_at,
            updated_at=updated_at
        )

        return m

    @classmethod
    def get(cls, id: int) -> PostsDTO:
        return PostsDTO(
                    id = 0,
                    title = faker.word(),
                    content=faker.text(),
                    created_at=faker.date_time(),
                    updated_at=faker.date_time()

                )
