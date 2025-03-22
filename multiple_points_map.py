import folium

# 예시 데이터: 식별자, 위도, 경도
data = [
    {"id": "A", "lat": 37.5665, "lon": 126.9780},
    {"id": "B", "lat": 37.5700, "lon": 126.9768},
    {"id": "C", "lat": 37.5650, "lon": 126.9820}
]

# 지도 중심을 데이터의 평균 좌표로 설정
center_lat = sum(item["lat"] for item in data) / len(data)
center_lon = sum(item["lon"] for item in data) / len(data)
m = folium.Map(location=[center_lat, center_lon], zoom_start=15)

# 각 좌표에 마커 추가
for item in data:
    folium.Marker(
        location=[item["lat"], item["lon"]],
        popup=f'식별자: {item["id"]}',
        tooltip=item["id"]  # 마우스 오버 시 식별자 표시
    ).add_to(m)

# HTML 파일로 저장 (브라우저에서 열면 지도 확인 가능)
m.save("multiple_points_map.html")
