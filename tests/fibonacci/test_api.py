def test_up_to_including_index(test_app):
    rv = test_app.get("/api/fibonacci/up-to-including-index?n=8")
    assert rv.status_code == 200
    assert rv.json == [0, 1, 1, 2, 3, 5, 8, 13, 21]
