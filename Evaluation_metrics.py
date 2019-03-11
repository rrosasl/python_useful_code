'''
Accuracy
accuracy = (# items labeled correctly) / (all items)
    short comings: not ideal for skewed classes, or if you have a strong preference towards minimizing either type 1 or type 2 error (e.g. innocent until proven guilty)

Confusion Matrix
    2x2 Matrix (x= actual class [positive/negative], y=predicted class [positive, negative])
        top_left: pred_positive, act_positive
        top_right: pred_positive, act_negative
        bottom_left: pred_negative, act_positive
        bottom_right: pred_negative, act_negative

Recall
    True positive / (True positive + False Negative)
        pred_positive,act_positive / (pred_positive,act_positive + pred_negative,act_positive)
    Out of all items that are truly positive, how many were correctly classified as positive

Precision
    True positive / (True Positive + False Positive)
        pred_positive,act_positive / (pred_positive,act_positive + pred_positive,act_negative)
    Out of all the items that are labeled as positive, how many truly belong in that class

F1 score
    Average of precision and recall. 1 is best, 0 is worst
    F1 = 2 * (precision*recall) / (precision+recall)



'''
from sklearn.metrics import accuracy_score
accuracy_score(y_true, y_pred)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_true,y_pred)

from sklearn.metrics import precision_score
precision_score(y_true, y_pred)

from sklearn.metrics import recall_score
recall_score(y_true, y_pred)

from sklearn.metrics import f1_score
f1_score(y_true,y_pred)
