from django.db import models
#A regime will be scheduled on the terminal
class Regimes(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)    
    question = models.ManyToManyField(to='quality_control.Questions', blank=True, help_text = "A regime can have multiple questions")
    sequenceno = models.PositiveIntegerField(default=0)
    is_deleted = models.BooleanField(default="False", blank=True) 

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()

    class Meta:
        db_table = 'AV_REGIMES'

class Questions(models.Model):
    question = models.CharField(max_length=50)

    class Meta:
        db_table = 'AV_QUESTIONS'

class Answers(models.Model):
    question = models.ForeignKey("Questions", related_name="questions", on_delete = models.CASCADE)
    choice = models.CharField(max_length=50)
    position = models.IntegerField("position")

    class Meta:
        db_table = 'AV_ANSWERS'
        unique_together = [
            # no duplicated choice per question
            ("question", "choice"), 
            # no duplicated position per question 
            ("question", "position") 
        ]
        ordering = ("position",)
        