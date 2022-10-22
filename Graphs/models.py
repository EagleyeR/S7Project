from django.db import models

# class GetData(CreateView):
#     template_name = 'Graphs/getData.html'
#     form_class = StartForm
#     success_url = reverse_lazy('index')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["constant"] = FIELDS_CONST
#         return context

class Yarik(models.Model):
    aircraft_id = models.TextField(verbose_name="aircraft id", null=True, blank=True)
    engine_position = models.TextField(verbose_name="engine position", null=True, blank=True)
    n1_modifier = models.TextField(verbose_name="n1 modifier", null=True, blank=True)
    number_blades = models.TextField(verbose_name="number blades", null=True, blank=True)
    engine_family = models.TextField(verbose_name="engine family", null=True, blank=True)
    engine_type = models.TextField(verbose_name="engine type", null=True, blank=True)
    manufacturer = models.TextField(verbose_name="manufacturer", null=True, blank=True)
    ZHPTAC = models.TextField(verbose_name="HPT ACTIVE CLEARANCE CNTL", null=True, blank=True)
    ZLPTAC = models.TextField(verbose_name="LPT ACTIVE CLEARANCE CNTL", null=True, blank=True)
    ZPCN12 = models.TextField(verbose_name="N1 INDICATED", null=True, blank=True)
    ZPCN25 = models.TextField(verbose_name="N2 (HIGH SPEED ROTOR)", null=True, blank=True)
    ZPHSF = models.TextField(verbose_name="PHASE ANGLE", null=True, blank=True)
    ZPHSR = models.TextField(verbose_name="PHASE ANGLE (REAR)", null=True, blank=True)
    ZPN12R = models.TextField(verbose_name="CORRECTED N1 INPUT FROM FADEC (%RPM)", null=True, blank=True)
    ZPOIL = models.TextField(verbose_name="OIL PRESSURE (PSI)", null=True, blank=True)
    ZPS3 = models.TextField(verbose_name="PS13 (FAN OGV DISCHARGE)", null=True, blank=True)
    ZT1AB = models.TextField(verbose_name="FAN INLET TOTAL TEMPERATURE FROM FADEC (DEG C)']", null=True, blank=True)
    ZT3 = models.TextField(verbose_name="HPC DISCHARG TOT TEMP (DEG)", null=True, blank=True)
    ZT49 = models.TextField(verbose_name="EGT-HPT DISCHRG TOT TMP(DEG)", null=True, blank=True)
    ZTAMB = models.TextField(verbose_name="STATIC AIR TEMPERATURE FROM FADEC (DEG R)", null=True, blank=True)
    ZTLA = models.TextField(verbose_name="THROTTLE LEVER ANGLE(DEG)", null=True, blank=True)
    ZTNAC = models.TextField(verbose_name="NACELLE TEMP(DEG C)", null=True, blank=True)
    ZTOIL = models.TextField(verbose_name="OIL TEMP (DEG C)", null=True, blank=True)
    ZVB1F = models.TextField(verbose_name="VIB FAN/LO SPD (FAN PICKUP)", null=True, blank=True)
    ZVB1R = models.TextField(verbose_name="VIB LPT/LOW SPD(REAR PICKUP)", null=True, blank=True)
    ZVB2F = models.TextField(verbose_name="VIB COR/HI SPD (FAN PICKUP)", null=True, blank=True)
    ZVB2R = models.TextField(verbose_name="VIB HPT/HI SPD (REAR PICKUP)", null=True, blank=True)
    ZVSV = models.TextField(verbose_name="INDICATED_AIR_SPEED", null=True, blank=True)
    ZWF36 = models.TextField(verbose_name="VAR STATOR VANES POS (VAR)", null=True, blank=True)
    IHPSOV = models.TextField(verbose_name="PACK FLOW 1", null=True, blank=True)
    aircraft_family = models.TextField(verbose_name="aircraft family", null=True, blank=True)
    aircraft_type = models.TextField(verbose_name="aircraft type", null=True, blank=True)
    aircraft_grp = models.TextField(verbose_name="aircraft grp", null=True, blank=True)
    ac_manufacturer = models.TextField(verbose_name="ac manufacturer", null=True, blank=True)
    AGW = models.TextField(verbose_name="ACTUAL GROSS WEIGHT (LB)", null=True, blank=True)
    CAS = models.TextField(verbose_name="COMPUTED AIR SPEED (KNOTS)", null=True, blank=True)
    IAI = models.TextField(verbose_name="WING A/I", null=True, blank=True)
    IVS12 = models.TextField(verbose_name="ISOLATION VALVE SWITCH 1-2", null=True, blank=True)
    SAT = models.TextField(verbose_name="STATIC AIR TEMPERATURE (SAT)", null=True, blank=True)
    ZALT = models.TextField(verbose_name="PRESSURE ALTITUDE (FEET)", null=True, blank=True)
    ZT1A = models.TextField(verbose_name="TOTAL AIR TEMP (DEG C)", null=True, blank=True)
    ZVIAS = models.TextField(verbose_name="INDICATED_AIR_SPEED", null=True, blank=True)
    ZWBP1 = models.TextField(verbose_name="PACK FLOW 1", null=True, blank=True)
    ZWBP1_8E = models.TextField(verbose_name="CF34-8E PACK FLOW 1 - NOT USED BY BLEED ADJUSTMENT", null=True, blank=True)
    ZWBP2 = models.TextField(verbose_name="PACK FLOW 2", null=True, blank=True)
    ZWBP2_8E = models.TextField(verbose_name="CF34-8E PACK FLOW 2 - NOT USED BY BLEED ADJUSTMENT", null=True, blank=True)
    ZXM = models.TextField(verbose_name="MACH", null=True, blank=True)
    IBE = models.TextField(verbose_name="ENG BLEED VALVE ENG 1", null=True, blank=True)
    IBP = models.TextField(verbose_name="PACK VALVE 1", null=True, blank=True)
    IAIE = models.TextField(verbose_name="ENG ANTI-ICE SETTING", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Все данные'
        verbose_name = "Данные"
        ordering = ['-aircraft_id']
