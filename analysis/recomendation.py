def generate_recommendations(cluster_label, score):
    if cluster_label == "High":
        if score < 8:
            return "Покращувати ефективність"
        else:
            return "Молодець! Спробуй складніші проєкти!"

    elif cluster_label == "Medium":
        if score < 6:
            return "Практикуй більше годин"
        else:
            return "Майже молодець! Сфокуйсуватись на ефективності"

    elif cluster_label == "Low":
        return "Не будь слабим. Збільшуй навчання!"