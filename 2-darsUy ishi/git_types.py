# Git, dasturiy ta'minotlarni versiyalarini boshqarish uchun ishlatiladigan keng tarqalgan tizimdir. Quyida Git komandalari
# va ularning tavsiflari keltirilgan:
#
# 1. git config
#    - Tavsifi: Git konfiguratsiyasini sozlash (foydalanuvchi nomi, elektron pochta va boshqalar).
#
# 2. git init
#    - Tavsifi: Yangi Git repozitoriyasini yaratish uchun ishlatiladi. Joriy papkada `.git` katalogini yaratadi.
#
# 3. git clone <repository>
#    - Tavsifi: Mavjud Git repozitoriyasini nusxalash. Bu komanda repozitoriyani lokal kompyuterga ko'chiradi.
#
# 4. git status
#    - Tavsifi: Repozitoriyadagi o'zgarishlar haqida ma'lumot beradi (yangi fayllar, tahrirlangan fayllar va boshqalar).
#
# 5. git config --global user.username <Name>
#    - Tavsifi: Bu foydalanuvchi ismini Git konfiguratsiyasida belgilaydi va u barcha commitlarda ishlatiladi.
#
# 6. git config --global user.email <Email>
#    - Tavsifi: Bu foydalanuvchi emailni Git konfiguratsiyasida belgilaydi va u barcha commitlarda ishlatiladi.
#
# 7. git add <file>
#    - Tavsifi: O'zgarishlarni staging area-ga (tayyorlash maydoniga) qo'shadi, ya'ni commit qilinishi uchun faylni belgilaydi.
#
# 8. git add .
#    -  Tavsifi: Barcha o'zgarishlarni staging area-ga (tayyorlash maydoniga) qo'shadi, ya'ni commit qilinishi uchun faylni belgilaydi.
#
# 9. git commit -m "message"
#    - Tavsifi: O'zgarishlarni commit qilish va ularni tasdiqlash. `"message"` qismlariga commitning qisqacha tavsifi yoziladi.
#
# 10. git push
#    - Tavsifi: Lokal repozitoriyadagi o'zgarishlarni masofaviy repozitoriyaga yuboradi.
#
# 11. git pull
#    - Tavsifi: Masofaviy repozitoriyadagi o'zgarishlarni lokal repozitoriyaga olish.
#
# 12. git fetch
#    - Tavsifi: Masofaviy repozitoriyadagi yangi ma'lumotlarni olish, ammo ularni lokal branch-ga qo'shmaydi.
#
# 13. git log
#    - Tavsifi: Repozitoriyaning commit tarixini ko'rsatadi.
#
# 14. git diff
#    - Tavsifi: O'zgarishlar orasidagi farqlarni ko'rsatadi.
#
# 15. git branch
#    - Tavsifi: Branch (filial) larni ko'rsatadi yoki yangi branch yaratadi.
#
# 16. git checkout <branch>
#    - Tavsifi: Ma'lum bir branch-ga o'tish yoki uni yaratish.
#
# 17. git merge <branch>
#    - Tavsifi: Boshqa branch-dan o'zgarishlarni hozirgi branch-ga birlashtiradi.
#
# 18. git reset <file>
#    - Tavsifi: Staging area-dan faylni olib tashlaydi, ammo fayldagi o'zgarishlarni saqlaydi.
#
# 19. git reset --hard
#    - Tavsifi: Barcha o'zgarishlarni bekor qiladi va so'nggi commit holatiga qaytadi.
#
# 20. git rm <file>
#    - Tavsifi: Faylni Git repo-sidan olib tashlaydi va uning o'zgarishlarini staging area-ga qo'shadi.
#
# 21. git stash
#    - Tavsifi: Hozirgi o'zgarishlarni vaqtincha saqlaydi va toza ish holatiga qaytadi.
#
# 22. git stash pop
#    - Tavsifi: Oldingi `git stash` bilan saqlangan o'zgarishlarni qaytaradi.
#
# 23. git tag
#    - Tavsifi: Repozitoriyaning ma'lum commit-lariga belgi qo'yish.
#
# 24. git config --list
#    - Tavsifi: Git konfiguratsiyasini barcha sozlamalirini ro'yxat shaklida ko'rsatadi.
#
# 25. git version
#    - Tavsifi:  Git konfiguratsiyasini versiasini ko'rsatadi.