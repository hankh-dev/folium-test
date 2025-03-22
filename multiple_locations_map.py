import folium
from folium.plugins import MarkerCluster

# 예시로 사용할 (위도, 경도) 좌표 목록
coords = [
    (37.5665, 126.9780),  # 서울시청 근처
    (37.5704, 126.9924),  # 종로 주변
    (37.5608, 126.9835),  # 광화문 근처
    (35.1795, 129.0756),  # 부산
    (36.3504, 127.3845),  # 대전
    (35.8685, 128.6057),  # 대구
    (37.4558, 126.7052),  # 인천
    (33.4996, 126.5312)   # 제주
]

# 1) 지도의 초기 중심 좌표를 잡기 위한 방법
#    - 첫 번째 좌표를 지도 중앙으로, 혹은 여러 좌표의 평균값을 사용할 수 있습니다.
center_lat = coords[0][0]
center_lon = coords[0][1]

# 2) folium.Map 객체 생성
m = folium.Map(location=[center_lat, center_lon], zoom_start=7)

# 3) MarkerCluster 객체 생성
marker_cluster = MarkerCluster().add_to(m)

# 4) 좌표 목록을 순회하면서 마커 추가
for lat, lon in coords:
    folium.Marker(
        location=[lat, lon],
        popup=f"위도: {lat}, 경도: {lon}"
    ).add_to(marker_cluster)

# 5) 지도 저장
m.save("multiple_locations_map.html")

print("지도 생성이 완료되었습니다. 'multiple_locations_map.html' 파일을 열어보세요.")

