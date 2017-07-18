from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):
    state = models.CharField(max_length=9)
    user_id_x = models.ForeignKey(User, on_delete=models.CASCADE, related_name="xgames")
    user_id_o = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ogames")

    # TODO defualt=null here?
    winner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wins")
    turn_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="turns")
    is_over = models.BinaryField()

    def __str__(self):
        return ' '.join([self.user_id_x.__str__(), self.user_id_o.__str__(), self.state])
