# Aday_Mühendislik_Case
Aday_Mühendislik_Case
Veriseti Açıklaması
1) Flight
2) Uçuşa ait bilgiler
  flight_id: Uçuş ID
  model_id: Uçak model ID,
  mission_id: Misyon ID,
  flight_date: Uçuş zamanı,
  landing_date: İniş zamanı,
  landing_success: Başarılı iniş durumu,
  flight_success: Başarılı kalkış durumu,
  flight_county: Uçuş yapılan ilçe,
  flight_province: Uçuş yapılan il,
  flight_region: Uçuş yapılan bölge,
  real_flight_time: Yerden kalkış ve yere temas arasında geçen süre,
  mission_success : Uçuş sırasında ifa edilen görevin başarı durumu
  2) Angular_velocity:
  Otopilot tarafından üretilen açısal hızlar.
  flight_id : Uçuş ID,
  time: Uçuş sırasında kayıt edilen zaman,
  xyz[0]: X koordinatındaki hızlanma açısı,
  xyz[1]: Y koordinatındaki hızlanma açısı,
  xyz[2]: Z koordinatındaki hızlanma açısı,
  type: Otopilotun yazdığı dosya ismi.
  3) GPS
  GPS sensöründen gelen verileri içerir.
  flight_id: Uçuş ID,
  time: Uçuş sırasında kayıt edilen zaman,
  lat: latitude,
  lon: longitude,
  alt: altitude
