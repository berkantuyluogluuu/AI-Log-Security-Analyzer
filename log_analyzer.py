import os
import re
from datetime import datetime

# Dosya yolları
LOG_FILE = "server_logs.txt"
REPORT_FILE = "security_report.html"

# Saldırı tespit kuralları (Regex / Anahtar Kelimeler)
RULES = {
    "Brute Force (Kaba Kuvvet)": r"Failed password",
    "SQL Injection (Veritabanı Saldırısı)": r"UNION SELECT|OR 1=1",
    "Port Scanning (Nmap Tarama)": r"Nmap port scanning"
}

def analyze_logs():
    if not os.path.exists(LOG_FILE):
        print(f"Hata: {LOG_FILE} bulunamadı! Lütfen log dosyasını klasöre ekleyin.")
        return

    detected_alerts = []
    stats = {"Brute Force (Kaba Kuvvet)": 0, "SQL Injection (Veritabanı Saldırısı)": 0, "Port Scanning (Nmap Tarama)": 0}

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            for attack_type, pattern in RULES.items():
                if re.search(pattern, line, re.IGNORECASE):
                    detected_alerts.append({
                        "time": line[:19],
                        "type": attack_type,
                        "details": line.strip()
                    })
                    stats[attack_type] += 1
                    break

    generate_html_report(detected_alerts, stats)

def generate_html_report(alerts, stats):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # HTML Şablonu (Şık ve modern siber güvenlik teması - Dark Mode)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>Siber Güvenlik Log Analiz Raporu</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #1a1a24; color: #e1e1e6; margin: 40px; }}
            h1 {{ color: #ff4a5a; border-bottom: 2px solid #2f2f3d; padding-bottom: 10px; }}
            .summary {{ display: flex; gap: 20px; margin-bottom: 30px; }}
            .card {{ background-color: #23232f; border-left: 5px solid #ff4a5a; padding: 15px; border-radius: 4px; flex: 1; }}
            .card.safe {{ border-left-color: #2ecc71; }}
            .card h3 {{ margin: 0 0 10px 0; color: #8a8a9e; }}
            .card p {{ margin: 0; font-size: 24px; font-weight: bold; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background-color: #23232f; border-radius: 4px; overflow: hidden; }}
            th, td {{ padding: 12px 15px; text-align: left; }}
            th {{ background-color: #2f2f3d; color: #ff4a5a; text-transform: uppercase; font-size: 13px; }}
            tr {{ border-bottom: 1px solid #1a1a24; }}
            tr:hover {{ background-color: #2a2a38; }}
            .badge {{ background-color: #ff4a5a; color: white; padding: 3px 8px; border-radius: 3px; font-size: 12px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>🛡️ Otomatik Güvenlik Log Analiz Raporu</h1>
        <p><strong>Rapor Oluşturulma Tarihi:</strong> {now} | <strong>Durum:</strong> İnceleme Tamamlandı</p>
        
        <div class="summary">
            <div class="card">
                <h3>Toplam Tespit Edilen Saldırı</h3>
                <p style="color: #ff4a5a;">{len(alerts)}</p>
            </div>
            <div class="card">
                <h3>Brute Force / SQLi / Nmap</h3>
                <p>{stats['Brute Force (Kaba Kuvvet)']} / {stats['SQL Injection (Veritabanı Saldırısı)']} / {stats['Port Scanning (Nmap Tarama)']}</p>
            </div>
        </div>

        <h2>🚨 Kritik Güvenlik Olayları (Log Kayıtları)</h2>
        <table>
            <thead>
                <tr>
                    <th>Zaman Damgası</th>
                    <th>Saldırı Tipi</th>
                    <th>Log Detayı</th>
                </tr>
            </thead>
            <tbody>
    """
    
    for alert in alerts:
        html_content += f"""
                <tr>
                    <td>{alert['time']}</td>
                    <td><span class="badge">{alert['type']}</span></td>
                    <td style="font-family: monospace; color: #ffcbd1;">{alert['details']}</td>
                </tr>
        """
        
    html_content += """
            </tbody>
        </table>
    </body>
    </html>
    """

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Başarılı! Güvenlik raporu oluşturuldu: {REPORT_FILE}")

if __name__ == "__main__":
    analyze_logs()