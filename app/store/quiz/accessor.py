from typing import Optional, List

from app.base.base_accessor import BaseAccessor
from app.quiz.models import Theme, Question, Answer


class QuizAccessor(BaseAccessor):
    async def create_theme(self, title: str) -> Theme:
        theme = Theme(id=self.app.database.next_theme_id, title=str(title))
        self.app.database.themes.append(theme)
        return theme

    async def get_theme_by_title(self, title: str) -> Optional[Theme]:
        for theme in self.app.database.themes:
            if theme.title.lower() == title.lower():
                return theme
        return None

    async def get_theme_by_id(self, id_: int) -> Optional[Theme]:
        try:
            return self.app.database.themes[int(id_)-1]
        except IndexError:
            return None

    async def list_themes(self) -> List[Theme]:
        return self.app.database.themes

    async def get_question_by_title(self, title: str) -> Optional[Question]:
        for question in self.app.database.questions:
            if question.title.lower() == title.lower():
                return question
        return None

    async def create_question(
        self, title: str, theme_id: int, answers: List[Answer]
    ) -> Question:
        question = Question(
            id=self.app.database.next_question_id,
            title=str(title),
            theme_id=theme_id,
            answers=answers,
        )
        self.app.database.questions.append(question)
        return question

    async def list_questions(self, theme_id: Optional[int] = None) -> List[Question]:
        if theme_id:
            return list(
                filter(lambda q: q.theme_id == theme_id, self.app.database.questions)
            )
        return self.app.database.questions
