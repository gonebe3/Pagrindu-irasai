from pirmas_atsiskaitymas.Servises.failu_valdymo_servisas import ikelti_duomenis, issaugoti_duomenis

#python -m pirmas_atsiskaitymas.testavimas

knygos = ikelti_duomenis("knygos.pickle")
skaitytojai = ikelti_duomenis("skaitytojai.pickle")


if skaitytojai and knygos:
    skaitytojas = skaitytojai[0]     
    knyga = knygos[5]                

    skaitytojas.prideti_paimta_knyga(knyga.unikalus_id)

    # Darome ja veluojancia (data praeityje)
    from datetime import datetime, timedelta
    skaitytojas.paimtos_knygos[-1]["Grazinti_iki"] = datetime.now() - timedelta(days=5)
    skaitytojas.paimtos_knygos[-1]["Ar_grazinta"] = False

    # Issaugome atnaujintus duomenis
    issaugoti_duomenis(skaitytojai, "skaitytojai.pickle")
    print("Testinė vėluojanti knyga pridėta.")

else:
    print("Trūksta bent vieno skaitytojo ar knygos duomenų!")


    Bibliotekininko meniu (Antaniux Antaniux)
1. Prideti nauja knyga
2. Pasalinti knyga pagal ID
3. Pasalinti senas knygas pagal metus
4. Perziureti visas knygas
5. Perziureti visus skaitytojus
6. Registruoti nauja skaitytoja
7. Statistika
8. Perziureti visas veluojancias knygas
9. Populiariausi zanrai pagal paemimus
10. Atgal