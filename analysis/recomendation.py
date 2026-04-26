def generate_recommendations(cluster_label, score):
    if cluster_label == 2:
        if score < 8:
            return "Покращувати ефективність"
        else:
            return "Молодець! Спробуй складніші проєкти!"

    elif cluster_label == 1:
        if score < 6:
            return "Практикуй більше годин"
        else:
            return "Майже молодець! Сфокуйсуватись на ефективності"

    elif cluster_label == 0:
        return "Не будь слабим. Збільшуй навчання!"